import os

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from sqlalchemy import desc, asc

from data_models import db, Author, Book
from data_population import data_population

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data", "library.sqlite")}'
CORS(app, resources={r"/api/*": {"origins": "*"}})

db.init_app(app)


@app.get("/api/v1/populate")
def get_populate_database():
    populate_database()

    return jsonify([
        book.to_dict()
        for book in db.session.query(Book).join(Author).all()
    ])


@app.get("/")
def get_home():
    sort_by = request.args.get("sort_by", "id")
    sort_order = request.args.get("sort_order", "desc")

    if sort_by == "author":
        sort_by_clause = desc(Author.name) if sort_order == "desc" else asc(Author.name)
    else:
        sort_by_clause = desc(sort_by) if sort_order == "desc" else asc(sort_by)

    books = [
        book.to_dict()
        for book in db.session.query(Book)
        .join(Author)
        .order_by(sort_by_clause)
        .all()
    ]
    return render_template("home.html", books=books), 200


@app.get("/api/v1/authors")
def get_authors():
    return jsonify([
        author.to_dict()
        for author in db.session.query(Author).join(Book).order_by(Author.id.desc()).all()
    ]), 200


@app.post("/api/v1/authors")
def add_author():
    body = request.json
    if not body:
        return jsonify({
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


@app.delete("/api/v1/authors/<int:author_id>")
def delete_author(author_id: int):
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()

    return jsonify({
        "message": f"Author with id {author_id} and all related books deleted successfully"
    }), 200


@app.get("/book/<int:book_id>")
def get_book_by_id(book_id: int):
    book = db.session.query(Book).join(Author).filter(Book.id == book_id).one()
    return render_template("book_detail.html", book=book)


@app.get("/api/v1/books")
def get_books():
    return jsonify([
        book.to_dict()
        for book in db.session.query(Book).join(Author).all()
    ])


@app.get("/api/v1/books/search")
def get_books_by_search():
    search_string = request.args.get("q", "")
    query = db.session.query(Book).join(Author)

    if search_string:
        query = query.filter(
            (Book.title.ilike(f"%{search_string}%")) |
            (Author.name.ilike(f"%{search_string}%"))
        )

    return jsonify([
        book.to_dict()
        for book in query.all()
    ])


@app.post("/api/v1/books")
def add_book():
    body = request.json

    if not body:
        return jsonify({
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


@app.delete("/api/v1/books/<int:book_id>")
def delete_book(book_id: int):
    db.session.query(Book).filter(Book.id == book_id).delete()
    db.session.commit()

    return jsonify({
        "message": f'Successfully deleted book with id {book_id}'
    })


def populate_database():
    data_population(app)


with app.app_context() as app_context:
    db.create_all()

if __name__ == "__main__":
    app.run("0.0.0.0", port=3000, debug=True)
