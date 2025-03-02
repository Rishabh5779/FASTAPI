

# main.py
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from models import Book
from database import get_db
from bson import ObjectId

app = FastAPI()

db = get_db()
collection = db["books"]

@app.post("/books/")
def create_book(book: Book):
    book_dict = book.dict()
    result = collection.insert_one(book_dict)
    return {"id": str(result.inserted_id), "message": "Book added successfully"}

@app.get("/books/")
def get_books():
    books = list(collection.find())
    for book in books:
        book["id"] = str(book["_id"])
        del book["_id"]
    return books

@app.get("/books/{book_id}")
def get_book(book_id: str):
    book = collection.find_one({"_id": ObjectId(book_id)})
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book["id"] = str(book["_id"])
    del book["_id"]
    return book

@app.put("/books/{book_id}")
def update_book(book_id: str, book: Book):
    result = collection.update_one({"_id": ObjectId(book_id)}, {"$set": book.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book updated successfully"}

@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    result = collection.delete_one({"_id": ObjectId(book_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}