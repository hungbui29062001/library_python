from library.extension import db
from sqlalchemy.orm import relationship

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    category_book_relationship = relationship("Book", back_populates="book_category_relationship")

    def __repr__(self) -> str:
        return f"<Category(id={self.id}, name={self.name})>"
