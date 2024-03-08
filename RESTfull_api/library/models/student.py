from library.extension import db

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    birth_date = db.Column(db.Date)
    gender = db.Column(db.Integer)
    class_name = db.Column(db.String(10), nullable = False)

    def __init__(self, name, birth_date, gender, class_name):
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.class_name = class_name