from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from data_models import db, Author, Book

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data", "library.sqlite")}'
CORS(app, resources={r"/api/*": {"origins": "*"}})

db.init_app(app)


@app.get("/api/v1/authors")
def get_authors():
    return [author.to_dict() for author in db.session.query(Author).order_by(Author.id.desc()).all()]


@app.post("/api/v1/authors")
def add_author():
    body = request.json
    if not body:
        return jsonify(
            {
                "message": "No valid data was submitted"
            }), 422

    author = Author(
        name=body.get("name"),
        birth_date=body.get("birth_date"),
        date_of_death=body.get("date_of_death")
    )

    db.session.add(author)
    db.session.commit()

    return jsonify(author.to_dict()), 200


@app.get("/api/v1/books")
def get_books():
    return [book.to_dict() for book in db.session.query(Book).all()]


@app.post("/api/v1/books")
def add_book():
    body = request.json

    if not body:
        return jsonify(
            {
                "message": "No valid data was submitted"
            }), 422

    book = Book(
        title=body.get("title"),
        isbn=body.get("isbn"),
        author_id=body.get("author_id"),
        publication_year=body.get("publication_year")
    )

    db.session.add(book)
    db.session.commit()

    return jsonify(book.to_dict()), 200


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run("0.0.0.0", port=3000, debug=True)
