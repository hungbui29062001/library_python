from library.extension import db
from library.library_ma import StudentSchema
from library.models.student import Student
from flask import request, jsonify
from datetime import datetime

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