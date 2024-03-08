from flask import Blueprint
from library.services.student_service import add_student_service

studentsBlueprint = Blueprint('students', __name__, url_prefix='/student-management')

@studentsBlueprint.route('/add-student', methods=['POST'])
def add_student():
    return add_student_service()