from flask import Blueprint
from library.services.student_service import add_student_service, update_student_service, get_all_student_service
from flask_jwt_extended import jwt_required
from library.common.auth_middleware import token_required

studentsBlueprint = Blueprint('students', __name__, url_prefix='/student-management')

@studentsBlueprint.route('/add-student', methods=['POST'])
def add_student():
    return add_student_service()

@studentsBlueprint.put('/update-student')
def update_student():
    return update_student_service()

@studentsBlueprint.get('/get-all-student')
@jwt_required()
# @token_required
def get_all_student():
    return get_all_student_service()