# Flask Library Management System

This is a simple Flask-based application for managing a library. The application provides features to add, view, and delete authors and books, as well as fetch book recommendations from an external API.

## Features

- **Populate Database:** Populate the database with mock data for testing purposes.
- **AI Book Recommendation:** Fetch a book recommendation from a rapid-api endpoint using chatgpt.
- **Manage Authors:** Add, view, and delete authors.
- **Manage Books:** Add, view, and delete books.
- **Search Books:** Search for books by title or author.
- **Sortable Books List:** Sort books displayed on the landing page.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLAlchemy
- Requests
- Flask-CORS

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/GerritHillebrecht/masterschool-book-alchemy.git
2. Navigate to the project directory:
    ```bash
   cd your-project-directory
3. Install the required packages:
    ```bash
   pip install -r requirements.txt

### Running the Application
1. Start the Flask application:
    ```bash
   python main.py
2. Open your browser and navigate to:
    ```bash
   http://localhost:5002

## API Endpoints

### Populate Database

- **Endpoint:** `/api/v1/populate`
- **Method:** `GET`
- **Description:** Populates the database with mock data for testing.

### AI Book Recommendation

- **Endpoint:** `/api/v1/books/ai`
- **Method:** `GET`
- **Description:** Fetches a book recommendation from a rapid-api endpoint using chatgpt.

### View All Authors

- **Endpoint:** `/api/v1/authors`
- **Method:** `GET`
- **Description:** Returns all authors ordered by id.

### Add Author

- **Endpoint:** `/api/v1/authors`
- **Method:** `POST`
- **Description:** Adds a new author to the database.

### Delete Author

- **Endpoint:** `/api/v1/authors/<int:author_id>`
- **Method:** `DELETE`
- **Description:** Deletes an author and all related books based on the provided author_id.

### View All Books

- **Endpoint:** `/api/v1/books`
- **Method:** `GET`
- **Description:** Fetches all books from the database.

### Search Books

- **Endpoint:** `/api/v1/books/search`
- **Method:** `GET`
- **Description:** Returns filtered books based on the provided search string.

### Add Book

- **Endpoint:** `/api/v1/books`
- **Method:** `POST`
- **Description:** Adds a new book to the database.

### Delete Book

- **Endpoint:** `/api/v1/books/<int:book_id>`
- **Method:** `DELETE`
- **Description:** Deletes a book based on the provided book_id.


