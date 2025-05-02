from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel

app = FastAPI()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library_db"
)

class BookCreate(BaseModel):
    title: str
    isbn: str
    author_id: int

@app.post("/books/")
def add_book(book: BookCreate):
    cursor = db.cursor()
    try:
        cursor.execute(
            "INSERT INTO books (title, isbn, author_id) VALUES (%s, %s, %s)",
            (book.title, book.isbn, book.author_id)
        )
        db.commit()
        return {"message": "Book added successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()

@app.get("/books/")
def get_books():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    return cursor.fetchall()

@app.get("/books/{book_id}")
def get_book(book_id: int):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
    book = cursor.fetchone()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookCreate):
    cursor = db.cursor()
    try:
        cursor.execute(
            "UPDATE books SET title=%s, isbn=%s, author_id=%s WHERE book_id=%s",
            (book.title, book.isbn, book.author_id, book_id)
        )
        db.commit()
        return {"message": "Book updated"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
        db.commit()
        return {"message": "Book deleted"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()