from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class ToDictMixin:
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
    __abstract__ = True


class Author(BaseModel):
    __tablename__ = "authors"

    def __str__(self):
        return f'{self.name} ({self.birth_date}{f' - {self.date_of_death}' if self.date_of_death else ""})'

    def __repr__(self):
        print(vars(self))
        return f'Author(id = {self.id}, name = {self.name}, birth_date = {self.birth_date}, date_of_death = {self.date_of_death})'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.String, nullable=False)
    date_of_death = db.Column(db.String, nullable=True)
    books = db.relationship('Book', back_populates='author', lazy=True)
    created_at = db.Column(db.DateTime, server_default=func.current_timestamp())
    updated_at = db.Column(db.DateTime, server_default=func.current_timestamp())


class Book(BaseModel):
    __tablename__ = "books"

    def __str__(self):
        return f'{self.title} ({self.publication_year}) [{self.isbn}]'

    def __repr__(self):
        return f'Book(id = {self.id}, title = {self.title}, isbn = {self.isbn}, publication_year = {self.publication_year})'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String, unique=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    cover = db.Column(db.String, nullable=False)
    excerpt = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    author = relationship("Author", back_populates="books")
    publication_year = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.current_timestamp())
    updated_at = db.Column(db.DateTime, server_default=func.current_timestamp())
