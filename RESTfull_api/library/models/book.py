from library.extension import db
from library.common.json_serializable import JsonSerializable
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship

class Book(db.Model, JsonSerializable):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    page_count = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable = False)
    book_author_relationship = relationship("Author", back_populates="author_book_relationship", uselist=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable = False)
    book_category_relationship = relationship("Category", back_populates="category_book_relationship", uselist=False)