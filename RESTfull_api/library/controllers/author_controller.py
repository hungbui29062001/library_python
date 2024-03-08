from flask import Blueprint
from library.services.author_service import get_all_author_service, get_author_by_id_service, add_author_service, delete_author_service, update_author_service

authorBlueprint = Blueprint('authors', __name__, url_prefix='/author-management')

@authorBlueprint.route('/get-all-author', methods=['GET'])
def getAllAuthor():
    return get_all_author_service()

@authorBlueprint.route('/get-author-by-id', methods=['GET'])
def getAuthorById():
    return get_author_by_id_service()

@authorBlueprint.route('/add-author', methods=['POST'])
def addAuthor():
    return add_author_service()

@authorBlueprint.route('/delete-author/<int:id>', methods=['DELETE'])
def deleteAuthor(id):
    return delete_author_service(id)

@authorBlueprint.route('/update-author', methods=['PUT'])
def updateAuthor():
    return update_author_service()