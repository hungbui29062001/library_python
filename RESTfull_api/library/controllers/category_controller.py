from flask import Blueprint
from library.services.category_service import add_category_service

categoryBlueprint = Blueprint('categories', __name__, url_prefix='/category-management')

@categoryBlueprint.route('/add-category', methods=['POST'])
def add_category():
    return add_category_service()