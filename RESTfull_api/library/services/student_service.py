from library.extension import db
from library.library_ma import StudentSchema
from library.models.student import Student
from flask import request, jsonify
from datetime import datetime
from flask_jwt_extended import get_jwt

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

def add_student_service():
    data = request.json

    if not data and 'name' in data and 'birth_date' in data and 'gender' in data and 'class_name' in data:
        return jsonify({'message:': 'Request body missing'}), 400
    try:
        new_student = Student(data['name'], datetime.strptime(data['birth_date'],"%Y-%m-%d"), data['gender'], data['class_name'])
        db.session.add(new_student)
        db.session.commit()
        return student_schema.jsonify(new_student), 200
    except IndentationError:
        db.session.rollback()
        return jsonify({'message:': 'Add failed'}), 500
    
def update_student_service():
    data = request.json

    student = Student.query.filter_by(id = data['id'])

    if student == None:
        return jsonify({'message:': 'Not found student'}), 404 
    try:
        student.name = data['name']
        
        return student_schema.jsonify(student), 200
    except IndentationError:
        db.session.rollback()
        return jsonify({'message:': 'Add failed'}), 500
    
def get_all_student_service():
    permission = get_jwt()
    if permission.get('is_owner') is True:
        data = request.get_json()

        students = Student.query.paginate(
            page = data.get('page'),
            per_page = data.get('per_page')
        )

        return students_schema.jsonify(students), 200
    else:
        return jsonify({'message': 'You are not authorized to access this'}), 401