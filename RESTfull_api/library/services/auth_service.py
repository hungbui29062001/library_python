from library.extension import db
from .student_service import student_schema
from flask import request, jsonify
from library.models.student import Student, TokenBlockList
from datetime import datetime
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt, current_user, get_jwt_identity

def register_service():
    data = request.json
    if not data and ('name' in data and 'birth_date' in data and 'gender' in data and 'class_name' in data and 'email' in data and 'password' in data):
        return jsonify({'message:': 'Request body missing'}), 400

    try:
        student = Student(name = data['name'], birth_date = datetime.strptime(data['birth_date'],"%Y-%m-%d"), gender = data['gender'], class_name = data['class_name'], email = data['email'])
        student.set_password(data['password'])
        student.add()
        return student_schema.jsonify(student), 200
    except IndentationError:
        db.session.rollback()
        return jsonify({'message:': 'Add failed'}), 500
    
def login_service():
    data = request.get_json()
    student = Student.get_user_by_email(data.get('email'))
    
    if student is None:
        return jsonify({'message:': 'Invalid email or password'}), 404
    check_password = student.check_password(data.get('password'))
    if check_password is True:
        access_token = create_access_token(identity=student.email)
        refresh_token = create_refresh_token(identity=student.email)
        return jsonify(
                {
                    'message:': 'login success',
                    'token': {
                        "access_token": access_token,
                        "refresh_token": refresh_token
                    }
                }
            ), 200
    else:
        return jsonify({'message:': 'Invalid email or password'}), 400

def whoami_service():
    claims = get_jwt()
    student = current_user

    return jsonify(
        {
            'current_user': student.toJson(),
            'claims': claims,
        }), 200

def refresh_token_service():
    identity = get_jwt_identity()

    new_access_token = create_access_token(identity=identity)

    return jsonify(
        {
            'access_token:': new_access_token
        }), 200

def logout_service():
    jwt = get_jwt()
    jti = jwt['jti']
    token = TokenBlockList(jti=jti)
    token.save()
    return jsonify(
        {
            'message:': 'Loged Out Seccessfully'
        }), 200
