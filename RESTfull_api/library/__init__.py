from flask import Flask, jsonify
from .extension import db, ma, jwt
from .models.student import Student, TokenBlockList
from .models.author import Author
from .models.category import Category
from .controllers.book_controller import booksBlueprint
from .controllers.author_controller import authorBlueprint
from .controllers.borrow_controller import borrowsBlueprint
from .controllers.students_controller import studentsBlueprint
from .controllers.category_controller import categoryBlueprint
from .controllers.auth_controller import auth_bp
from .controllers.image_controller import image_bp
import os
from datetime import date
from library.services.student_service import student_schema

def init_data():
    # db.session.add(Student(name='Student 1', birth_date=date(2001, 6, 29), gender=0, class_name='class 1', email='email', password='password'))

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
    app.register_blueprint(auth_bp)
    app.register_blueprint(image_bp)

def create_db(app):
    if not os.path.exists('instance/library.db'):
        with app.app_context():
            db.create_all()
            db.session.commit()
            print('------------ Start init data ------------')
            init_data()
            print('------------ End init data ------------')

def handle_error_jwt():
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify({'message' : 'Token has expired!'}), 401
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({'message' : 'Invalid Authentication token!'}), 401
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({'message' : 'Authentication Token is missing!'}), 401
    @jwt.additional_claims_loader
    def make_additional_claims(identity):
        if identity == 'lapulga29062001@gmail.com':
            return {'is_owner': True}
        return {'is_owner': False}
    @jwt.user_lookup_loader
    def user_lookup_callback(jwt_header, jwt_data):
        identity = jwt_data['sub']
        return Student.query.filter_by(email=identity).one_or_none()
    @jwt.token_in_blocklist_loader
    def token_in_blocklist_callback(jwt_header, jwt_data):
        jti = jwt_data['jti']

        token = db.session.query(TokenBlockList).filter(TokenBlockList.jti == jti).scalar()
        return token is not None
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_data):
        return jsonify({'message' : 'Token has been revoked!'}), 401

def create_app(config_file = 'config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    create_db(app)
    blueprint_init(app)
    handle_error_jwt()
    return app