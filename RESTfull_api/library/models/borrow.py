from library.extension import db
from datetime import datetime

class Borrow(db.Model):
    __tablename__ = 'borrows'
    
    id = db.Column(db.Integer, primary_key = True)
    students_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable = False)
    books_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable = False)
    borrow_date = db.Column(db.Date, nullable = False, default = datetime.now().date())
    return_date = db.Column(db.Date, nullable = False)

    def __init__(self, name, books_id, borrow_date, return_date):
        self.name = name
        self.books_id = books_id
        self.borrow_date = borrow_date
        self.return_date = return_date