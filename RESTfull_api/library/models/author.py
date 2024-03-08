from library.extension import db
from sqlalchemy.orm import relationship

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    author_book_relationship = relationship("Book", back_populates="book_author_relationship")

    def __repr__(self) -> str:
        return f"<Author(id={self.id}, name={self.name})>"