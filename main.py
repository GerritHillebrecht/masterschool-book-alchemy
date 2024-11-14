from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from sqlalchemy.orm import joinedload
import os
from data_models import db, Author, Book

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
        for book in db.session.query(Book).all()
    ])


@app.get("/")
def get_home():
    books_with_authors = db.session.query(Book).join(Author).all()
    print("books")
    print("-----------------------------")
    for book in books_with_authors:
        print(book.to_dict())
    print("-----------------------------")

    books = [
        book.to_dict()
        for book in db.session.query(Book)
        .order_by(Book.id.desc())
        .all()
    ]
    return render_template("home.html", books=books), 200


@app.get("/api/v1/authors")
def get_authors():
    return [author.to_dict() for author in db.session.query(Author).order_by(Author.id.desc()).all()]


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


@app.get("/api/v1/books")
def get_books():
    return [book.to_dict() for book in db.session.query(Book).all()]


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


def populate_database():
    authors = [
        Author(
            name="Franz Kafka",
            birth_date="1883-07-03",
            date_of_death="1924-06-03"
        ),
        Author(
            name="Oscar Wilde",
            birth_date="1854-10-16",
            date_of_death="1900-11-30"
        ),
        Author(
            name="Stephen King",
            birth_date="1947-09-21"
        ),
        Author(
            name="Charles Dickens",
            birth_date="1812-02-07",
            date_of_death="1870-06-09"
        ),
        Author(
            name="Hermann Hesse",
            birth_date="1877-07-02",
            date_of_death="1962-08-09"
        )
    ]

    books = [
        Book(
            title="Die Verwandlung",
            isbn="9786589008231",
            author_id=1,
            publication_year=1915
        ),
        Book(
            title="Das Bildnis des Dorian Gray",
            isbn="9786555980004",
            author_id=2,
            publication_year=1915
        ),
        Book(
            title="Es",
            isbn="9783453435773",
            author_id=3,
            publication_year=1986
        ),
        Book(
            title="Oliver Twist",
            isbn="9780786177899",
            author_id=4,
            publication_year=1838
        ),
        Book(
            title="Der Steppenwolf",
            isbn="9783518031599",
            author_id=5,
            publication_year=1927
        ),
    ]

    with app.app_context():
        for row in [*authors, *books]:
            db.session.add(row)
        db.session.commit()


with app.app_context() as app_context:
    db.create_all()

if __name__ == "__main__":
    app.run("0.0.0.0", port=3000, debug=True)
