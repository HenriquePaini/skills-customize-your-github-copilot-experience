from fastapi import FastAPI

app = FastAPI(title="Books API")

books = [
    {
        "id": 1,
        "title": "The Pragmatic Programmer",
        "author": "Andy Hunt and Dave Thomas",
        "year": 1999,
    }
]


@app.get("/")
def read_root():
    """Return a health check for the API."""
    pass


@app.get("/books")
def list_books():
    """Return all books."""
    pass


# TODO: Create a Pydantic Book model.
# TODO: Add POST /books with validation and status code 201.
# TODO: Add GET, PUT, and DELETE /books/{book_id}.


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
