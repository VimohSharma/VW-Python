from flask import Blueprint, request, jsonify
from ..models import Book
from .. import db

library_bp = Blueprint("library", __name__)

@library_bp.route("/books", methods=["POST"])
def add_book():

    data = request.json

    book = Book(
        title=data["title"],
        author=data["author"],
        copies=data["copies"]
    )

    db.session.add(book)
    db.session.commit()

    return jsonify({"message": "Book added"})

@library_bp.route("/books", methods=["GET"])
def get_books():

    books = Book.query.all()

    result = []

    for b in books:
        result.append({
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "copies": b.copies
        })

    return jsonify(result)

@library_bp.route("/borrow/<int:id>")
def borrow_book(id):

    book = Book.query.get(id)

    if not book:
        return jsonify({"error": "Book not found"})

    if book.copies == 0:
        return jsonify({"message": "Book unavailable"})

    book.copies -= 1

    db.session.commit()

    return jsonify({"message": "Book borrowed"})

@library_bp.route("/books/unavailable")
def unavailable_books():

    books = Book.query.filter_by(copies=0).all()

    result = []

    for b in books:
        result.append({
            "id": b.id,
            "title": b.title
        })

    return jsonify(result)