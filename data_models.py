from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import as_declarative

db = SQLAlchemy()


# @as_declarative
# class Base(db.Model):
#     def to_dict(self):
#         return {c.name: getattr(self, c.name) for c in self.__table__.columns}
#     pass


class Author(db.Model):
    __tablename__ = "authors"

    def __str__(self):
        return f'{self.name} ({self.birth_date}{f' - {self.date_of_death}' if self.date_of_death else ""})'

    def __repr__(self):
        print(vars(self))
        return f'Author(id = {self.id}, name = {self.name}, birth_date = {self.birth_date}, date_of_death = {self.date_of_death})'

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.String, nullable=False)
    date_of_death = db.Column(db.String, nullable=True)
    books = db.relationship('Book', backref='authors', lazy=True)


class Book(db.Model):
    __tablename__ = "books"

    def __str__(self):
        return f'{self.title} ({self.publication_year}) [{self.isbn}]'

    def __repr__(self):
        return f'Book(id = {self.id}, title = {self.title}, isbn = {self.isbn}, publication_year = {self.publication_year})'

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String, unique=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    publication_year = db.Column(db.Integer)


if __name__ == "__main__":
    author = Author(
        name="Antonio Banderas",
        birth_date="1970"
    )

    print(author)
