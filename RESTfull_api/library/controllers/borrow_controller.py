from flask import Blueprint
from library.services.borrow_service import get_borrow_author_cat_service

borrowsBlueprint = Blueprint('borrows', __name__, url_prefix='/borrow-management')

@borrowsBlueprint.route('/get-borrows-by-student-name/<string:student_name>', methods=['GET'])
def get_borrow_author_cat(student_name):
    return get_borrow_author_cat_service(student_name)