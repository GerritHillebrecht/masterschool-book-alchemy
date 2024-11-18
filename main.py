"""
DISCLAIMER:
No pagination & no responsiveness. Mild Server-side-validation at best.
Since the app does not use text sql-queries and no raw queries, sqlalchemy's parameterization of
inputs is enough sanitization for now.
"""

import os

import requests
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from sqlalchemy import desc, asc
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, DataError, OperationalError
from werkzeug.exceptions import BadRequest

from data_models import db, Author, Book
from data_population import data_population

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data", "library.sqlite")}'
CORS(app, resources={r"/api/*": {"origins": "*"}})

db.init_app(app)


@app.get("/api/v1/populate")
def get_populate_database():
    """
    Populates an empty database with mock-data for testing.
    """
    data_population(app)

    return jsonify([
        book.to_dict()
        for book in db.session.query(Book).join(Author).all()
    ])


@app.get("/api/v1/books/ai")
def get_ai_recommendation():
    """
    Fetches a book recommendation from a rapid-api endpoint, which uses chatgpt.
    Uses the books in the database as a basis for the decision.
    Formats it as a javascript-object.
    """
    url = 'https://chat-gpt26.p.rapidapi.com/'
    books = ", ".join([
        f'{book.title} ({book.author.name}) ({book.publication_year})'
        for book in db.session.query(Book).join(Author).all()
    ])

    prompt = f"""
    Please give me for the following books a recommendation for a new book to read:
    {books}.
    Please provide your answer in the following format, and don't write anything else:
    ```
    {{
        "title": __TITLE__,
        "isbn": __ISBN__,
        "author"=__AUTHOR__,
        "rating"=__RATING__,
        "cover"=__COVER__,
        "excerpt"=__EXCERPT__,
        "publication_year"=__PUBLICATION_YEAR__
    }}
    ```
    For __COVER__ please find a valid link to a cover picture of the book.
    For __RATING__ just use a random number between 2 and 5.
    For __EXCERPT__ write a 3 sentence summary of the book please, without revealing the end.
    Thank you very much ;)
    """

    try:
        res = requests.post(
            url,
            headers={
                "Content-Type": "application/json",
                "x-rapidapi-key": "6a44209171mshcbb990bf9403ff1p1b8c9cjsn3fe5534b138a"
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            })
        res.raise_for_status()
        res_json = res.json()

        api_data = res_json.get("choices")[0].get("message").get("content")

        return jsonify(api_data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}),


@app.get("/")
def get_home():
    """
    The base route of the website. Renders and returns the landing page.
    Makes the displayed books sortable.
    """
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


@app.get("/books/add")
def add_book_page():
    """
    Renders a form to add a new book.
    """
    authors = db.session.query(Author).order_by(Author.name.asc()).all()
    return render_template("add_book.html", authors=authors)


@app.get("/authors/add")
def add_author_page():
    """
    Renders a form to add a new author.
    """
    return render_template("add_author.html")


@app.get("/api/v1/authors")
def get_authors():
    """
    Returns all Authors order by id.
    """
    return jsonify([
        author.to_dict()
        for author in db.session.query(Author).join(Book).order_by(Author.id.desc()).all()
    ]), 200


@app.post("/api/v1/authors")
def add_author():
    """
    Takes in form-data as json to add a new author.
    """
    try:
        body = request.form

        author = Author(
            name=body.get("name"),
            image=body.get("image"),
            birth_date=body.get("birth_date"),
            date_of_death=body.get("date_of_death")
        )

        db.session.add(author)
        db.session.commit()
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity error - Possible duplicate entry"}), 400
    except DataError:
        db.session.rollback()
        return jsonify({"error": "Data error - Invalid data format or value"}), 400
    except OperationalError:
        db.session.rollback()
        return jsonify({"error": "Operational error - Operational issue such as NOT NULL constraint"}), 500
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return redirect(url_for("get_home"))


@app.delete("/api/v1/authors/<int:author_id>")
def delete_author(author_id: int):
    """
    Deletes an author and all related books based on given author_id passed in via path.
    :param author_id: author id passed in via path.
    """
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()

    return jsonify({
        "message": f"Author with id {author_id} and all related books deleted successfully"
    }), 200


@app.get("/book/<int:book_id>")
def get_book_by_id(book_id: int):
    """
    Returns specific book data based on given id.
    :param book_id: Passed book id via path.
    """
    book = db.session.query(Book).join(Author).filter(Book.id == book_id).one()
    return render_template("book_detail.html", book=book)


@app.get("/api/v1/books")
def get_books():
    """
    Fetches all books from the database and returns them.
    """
    return jsonify([
        book.to_dict()
        for book in db.session.query(Book).join(Author).all()
    ])


@app.get("/api/v1/books/search")
def get_books_by_search():
    """
    Returns filtered books from the database based on a passed search-string.
     
    """
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
    """
    Adds a book by given query body.
    :return: The added book as a javascript object.
    """

    try:
        print(request.form)
        body = request.form

        book = Book(
            title=body.get("title"),
            isbn=body.get("isbn"),
            cover=body.get("cover"),
            rating=body.get("rating"),
            excerpt=body.get("excerpt"),
            author_id=body.get("author_id"),
            publication_year=body.get("publication_year")
        )
        print(book.to_dict())

        db.session.add(book)
        db.session.commit()
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity error - Possible duplicate entry"}), 400
    except DataError:
        db.session.rollback()
        return jsonify({"error": "Data error - Invalid data format or value"}), 400
    except OperationalError:
        db.session.rollback()
        return jsonify({"error": "Operational error - Operational issue such as NOT NULL constraint"}), 500
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return redirect(url_for("get_home"))


@app.delete("/api/v1/books/<int:book_id>")
def delete_book(book_id: int):
    """
    Deletes a book based on path id.
    :param book_id:
    """
    db.session.query(Book).filter(Book.id == book_id).delete()
    db.session.commit()

    return jsonify({
        "message": f'Successfully deleted book with id {book_id}'
    })


with app.app_context() as app_context:
    db.create_all()

if __name__ == "__main__":
    app.run("0.0.0.0", port=3000, debug=True)
