from library.extension import db
from library.library_ma import BooksSchema
from library.models.book import Book
from library.models.author import Author
from library.models.category import Category
from flask import request
from flask import jsonify
from sqlalchemy.sql import func, text
import json
# from flask_api import status
# from werkzeug.exceptions import NotFound, BadRequest

book_schema = BooksSchema()
books_schema = BooksSchema(many=True)

def add_book_service():
    name = request.json['name']
    page_count = request.json['page_count']
    author_id = request.json['author_id']
    category_id = request.json['category_id']

    author = Author.query.filter_by(id=author_id).first()
    if author == None:
        return jsonify({'message': 'Not found author'}), 404

    category = Category.query.filter_by(id=category_id).first()
    if category == None:
        return jsonify({'message': 'Not found category'}), 404

    try:
        new_book = Book(name=name, page_count=page_count, book_author_relationship=author, book_category_relationship=category)
        db.session.add(new_book)
        db.session.commit()
        return book_schema.jsonify(new_book), 200
    except IndentationError:
        db.session.rollback()
        return jsonify({'message': 'Add book failed'}), 404
    
def get_all_books_service():
    try:
        result = db.session.execute(text('select * from books'))
        # books = Book.query.all()
        if result:
            return books_schema.jsonify(result)
        else:
            return jsonify({'message': 'Not found book'}), 404
    except IndentationError:
        return 'Error'
    
def get_books_by_id_service(id):
    try:
        book = Book.query.get(id)
        if book:
            return book_schema.jsonify(book)
        else:
            return jsonify({'message': 'Not found book'}), 404
    except IndentationError:
        return 'Error'
    
def delete_book_service(id):
    book = Book.query.get(id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return book_schema.jsonify(book)
        except IndentationError:
            db.session.rollback()
            return 'Error'
    else:
        return jsonify({'message': 'Not found book'}), 404

def update_book_service():
    bookRequest = request.json
    if not (bookRequest and 'id' in bookRequest):
        return 'id is required', 400
    bookId = bookRequest['id']
    book = Book.query.get(bookId)
    if book:
        try:
            if bookRequest and 'name' in bookRequest:
                book.name = bookRequest['name']
            if bookRequest and 'page_count' in bookRequest:
                book.page_count = bookRequest['page_count']
            if bookRequest and 'author_id' in bookRequest:
                author = Author.query.filter_by(id=bookRequest['author_id']).first()
                if author == None:
                    return jsonify({'message': 'Not found author'}), 404
                else:
                    book.book_author_relationship = author
            if bookRequest and 'category_id' in bookRequest:
                category = Category.query.filter_by(id=bookRequest['category_id']).first()
                if author == None:
                    return jsonify({'message': 'Not found author'}), 404
                else:
                    book.book_category_relationship = category
            db.session.commit()
            return book_schema.jsonify(book)
        except IndentationError:
            db.session.rollback()
            return 'Error'
    else:
        return jsonify({'message': 'Not found book'}), 404
    
def delete_all_book_service():
    try:
        db.session.query(Book).delete()
        db.session.commit()
        return jsonify({'message': 'delete success'}), 200
    except IndentationError:
        db.session.rollback()
        return jsonify({'message': 'error'})
    
def get_book_by_author_id_service(id_request):
    books = Book.query.filter_by(author_id=id_request).all()
    if books:
        try:
            return books_schema.jsonify(books), 200
        except IndentationError:
            return jsonify({'message': 'error'}), 500
    else:
        return jsonify({'message': f"Not found books by {id_request}"}), 404

def get_book_by_author_name_service(name):
    books = Book.query.join(Author, Book.author_id==Author.id).filter(func.lower(Author.name) == name).all()
    if books:
        try:
            return books_schema.jsonify(books), 200
        except IndentationError:
            return jsonify({'message': 'error'}), 500
    else:
        return jsonify({'message': f"Not found books by {name}"}), 404
    