from flask import Blueprint
from library.services.image_service import upload_image_service

image_bp = Blueprint('image', __name__, url_prefix='/image-management')

@image_bp.post('/upload-image')
def upload_image():
    return upload_image_service()