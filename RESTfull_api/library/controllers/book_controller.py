from flask import Blueprint
from library.services.book_service import (add_book_service, get_all_books_service, get_books_by_id_service,
delete_book_service, update_book_service, delete_all_book_service, get_book_by_author_id_service, get_book_by_author_name_service)

booksBlueprint = Blueprint('books', __name__, url_prefix = '/book-management')

@booksBlueprint.route('/get-all-books', methods=['GET'])
def get_all_books():
    return get_all_books_service()

@booksBlueprint.route('/add-book', methods=['POST'])
def add_book():
    return add_book_service()

@booksBlueprint.route('/get-book-by-id/<int:id>', methods=['GET'])
def get_books_by_id(id):
    return get_books_by_id_service(id)

@booksBlueprint.route('/delete-book/<int:id>', methods=['DELETE'])
def delete_books(id):
    return delete_book_service(id)

@booksBlueprint.route('/update-book', methods=['PUT'])
def update_books():
    return update_book_service()

@booksBlueprint.route('/delete-all-book', methods=['DELETE'])
def delete_all_author():
    return delete_all_book_service()

@booksBlueprint.route('/get-book-by-authorid/<int:id_request>', methods=['GET'])
def get_book_by_author_id(id_request):
    return get_book_by_author_id_service(id_request)

@booksBlueprint.route('/get-book-by-author-name/<string:name>', methods=['GET'])
def get_book_by_author_name(name):
    return get_book_by_author_name_service(name)