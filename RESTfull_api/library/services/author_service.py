from library.extension import db
from library.library_ma import AuthorSchema
from library.models.author import Author
from library.models.book import Book
from flask import request, jsonify

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

def add_author_service():
    name = request.json['name']

    try:
        new_author = Author(name)
        db.session.add(new_author)
        db.session.commit()
        return author_schema.jsonify(new_author)
    except IndentationError:
        db.session.rollback()
        return jsonify({'message': 'Add failed'}), 500
    
def get_all_author_service():
    try:
        authors = Author.query.all()
        if authors:
            return authors_schema.jsonify(authors)
        else:
            return jsonify({'message': 'Not found author'}), 404
    except IndentationError:
        return jsonify({'message': 'Error'}), 500
    
def get_author_by_id_service(id):
    try:
        author = Author.query.get(id)
        if author:
            return author_schema.jsonify(author)
        else:
            return jsonify({'message': 'Not found author'}), 404
    except IndentationError:
        return jsonify({'message': 'Error'}), 500
    
def delete_author_service(id):
    author = Author.query.get(id)
    
    if author:
        try:
            books = Book.query.filter_by(author_id=id).all()
            if books != []:
                for item in books:
                    db.session.delete(item)
            db.session.delete(author)
            db.session.commit()
            return author_schema.jsonify(author)
        except IndentationError:
            db.session.rollback()
            return jsonify({'message': 'Error'}), 500
    else:
        return jsonify({'message': 'Not found author'}), 404

def update_author_service():
    request_body = request.json
    if not (request_body and 'id' in request_body):
        return jsonify({'message': 'id is required'}), 404
    authorId = request_body['id']
    author = Author.query.get(authorId)
    if author:
        try:
            if request_body and 'name' in request_body:
                author.name = request_body['name']
            db.session.commit()
            return author_schema.jsonify(author)
        except IndentationError:
            db.session.rollback()
            return jsonify({'message': 'Error'}), 500
    else:
        return jsonify({'message': 'Not found author'}), 404