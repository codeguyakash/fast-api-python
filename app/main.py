import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import os, platform, socket, sys
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

ENV = os.getenv("ENV")
APP_VERSION = '1.0.1'

class Book(BaseModel):
    id: int
    book: str
    author: str

books: List[Book]=[]

@app.get("/")
def read_root():
    return {
        "message": "Server is running using FastAPI",
        "app_version": APP_VERSION,
        "env": ENV,
    }

@app.get("/books")
def get_books():
    return books


@app.post("/books")
def create_book(book: Book):
    books.append(book)
    return book

@app.get("/books/{book_id}")
def get_book(book_id: int):
    return next((book for book in books if book.id == book_id), None)


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    for book in books:
        if book.id == book_id:
            book.book = book.book
            book.author = book.author
            return book
    return None

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    global books
    books = [book for book in books if book.id != book_id]
    return {"message": "Book deleted successfully"}  