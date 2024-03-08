from library.extension import db
from library.models.book import Book
from library.models.author import Author
from library.models.borrow import Borrow
from library.models.category import Category
from library.models.student import Student
from flask import jsonify
from sqlalchemy.sql import func

def get_borrow_author_cat_service(student_name):
    borrows = db.session.query(Borrow.id, Book.name, Author.name, Category.name).join(Student, Borrow.students_id == Student.id).join(
        Book, Book.id == Borrow.books_id).join(Author, Author.id == Book.author_id).join(Category, Category.id == Book.category_id).filter(
            func.lower(Student.name == student_name.lower())
        ).all()
    
    if borrows:
        return jsonify({f'{student_name} borrowed:': borrows}), 200
    else:
        return jsonify({'message:': 'Not found borrow!'}), 404