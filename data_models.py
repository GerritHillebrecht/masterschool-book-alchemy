from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class ToDictMixin:
    """
    Adds the "to_dict" functionality to Table-classes.
    Makes returning python dictionaries from these classes
    manageable.
    """

    # def __init__(self):
    #     self.__mapper__ = None
    #     self.__table__ = None
    #     self.id = None

    def to_dict(self, visited=None):
        # Prevent endless recursion
        if visited is None:
            visited = set()
        if self in visited:
            return {'id': self.id}

        visited.add(self)

        # Add table-columns with values to dict
        dict_representation = {
            c.name: getattr(self, c.name)
            for c in self.__table__.columns
        }

        # Add relationships if existing
        for rel in self.__mapper__.relationships:
            related_obj = getattr(self, rel.key)

            if related_obj is not None:
                if isinstance(related_obj, list):
                    dict_representation[rel.key] = [item.to_dict(visited) for item in related_obj]
                else:
                    dict_representation[rel.key] = related_obj.to_dict(visited)

        return dict_representation


class BaseModel(ToDictMixin, db.Model):
    """
    Custom Parent-class to extend from, easily extendable, especially useful
    for scalability.
    """
    __abstract__ = True


class Author(BaseModel):
    """
    Representation of the Author table.
    """
    __tablename__ = "authors"

    def __str__(self):
        return f'{self.name} ({self.birth_date}{f' - {self.date_of_death}' if self.date_of_death else ""})'

    def __repr__(self):
        # needed for line-length pep8 requirements
        author_id = self.id
        name = self.name
        dob = self.birth_date
        dod = self.date_of_death

        return f'Author(id = {author_id}, name = {name}, birth_date = {dob}, date_of_death = {dod})'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.String, nullable=False)
    date_of_death = db.Column(db.String, nullable=True)
    books = db.relationship('Book', back_populates='author', lazy=True, cascade="all, delete-orphan")
    created_at = db.Column(db.DateTime, server_default=func.current_timestamp())
    updated_at = db.Column(db.DateTime, server_default=func.current_timestamp())


class Book(BaseModel):
    """
    Representation of the Book table.
    """
    __tablename__ = "books"

    def __str__(self):
        return f'{self.title} ({self.publication_year}) [{self.isbn}]'

    def __repr__(self):
        # needed for line-length pep8 requirements
        book_id = self.id
        title = self.title
        isbn = self.isbn
        pub_year = self.publication_year

        return f'Book(id = {book_id}, title = {title}, isbn = {isbn}, publication_year = {pub_year})'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String, unique=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    cover = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    excerpt = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    author = relationship("Author", back_populates="books")
    publication_year = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.current_timestamp())
    updated_at = db.Column(db.DateTime, server_default=func.current_timestamp())
