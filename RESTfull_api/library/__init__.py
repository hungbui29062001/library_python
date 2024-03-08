from flask import Flask
from .extension import db, ma
from .models.student import Student
from .models.author import Author
from .models.category import Category
from .controllers.book_controller import booksBlueprint
from .controllers.author_controller import authorBlueprint
from .controllers.borrow_controller import borrowsBlueprint
from .controllers.students_controller import studentsBlueprint
from .controllers.category_controller import categoryBlueprint
import os
from datetime import date

def init_data():
    db.session.add(Student('Student 1', date(2001, 6, 29), 0, 'class 1'))
    db.session.add(Student('Student 2', date(2000, 1, 12), 0, 'class 2'))
    db.session.add(Student('Student 3', date(2000, 5, 2), 0, 'class 3'))

    db.session.add(Author(name='Author 1'))
    db.session.add(Author(name='Author 2'))
    db.session.add(Author(name='Author 3'))

    db.session.add(Category(name='Category 1'))
    db.session.add(Category(name='Category 2'))
    db.session.add(Category(name='Category 3'))
    db.session.commit()



def blueprint_init(app):
    app.register_blueprint(booksBlueprint)
    app.register_blueprint(authorBlueprint)
    app.register_blueprint(borrowsBlueprint)
    app.register_blueprint(studentsBlueprint)
    app.register_blueprint(categoryBlueprint)

def create_db():
    if not os.path.exists('RESTfull_api/instance/library.db'):
        db.create_all()
        print('------------ Start init data ------------')
        init_data()
        print('------------ End init data ------------')

def create_app(config_file = 'config.py'):
    app = Flask(__name__)
    with app.app_context():
        app.config.from_pyfile(config_file)
        db.init_app(app)
        ma.init_app(app)
        create_db()
        blueprint_init(app)
    return app