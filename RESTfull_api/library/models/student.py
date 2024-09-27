from library.extension import db
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone

class Student(db.Model):
    __tablename__ = 'students'

    # id = db.Column(db.String(), primary_key = True, default=str(uuid4()))
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    birth_date = db.Column(db.Date)
    gender = db.Column(db.Integer)
    class_name = db.Column(db.String(10), nullable = False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password=password)

    def check_password(self, password):
        return check_password_hash(self.password, password=password)
    
    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def toJson(self):
        return {
            'name': self.name,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'class_name': self.class_name,
            'email': self.email,
        }

class TokenBlockList(db.Model):
    __tablename__ = 'tokenblocklist'

    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(), nullable = True)
    created_at = db.Column(db.DateTime(), default = datetime.now(timezone.utc))

    def save(self):
        db.session.add(self)
        db.session.commit()

class Image(db.Model):
    __tablename__ = 'images'
    
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String(), nullable = True)