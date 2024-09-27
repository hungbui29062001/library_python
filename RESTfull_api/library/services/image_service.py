from library.extension import db
from library.library_ma import ImageSchema
from library.models.student import Image
from flask import flash, jsonify, request, current_app, config, send_from_directory
import os
from werkzeug.utils import secure_filename

image_schema = ImageSchema()
images_schema = ImageSchema(many=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_image_service():
    # check if the post request has the file part
    
    if 'file' not in request.files:
        flash('No file part')
        return jsonify({'message:': 'No file part'}), 401
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return jsonify({'message:': 'No selected file'}), 401
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        uploads_path = current_app.instance_path + str(current_app.config['UPLOAD_FOLDER'])
        file.save(os.path.join(uploads_path, filename))
        return send_from_directory(uploads_path, filename)
        return jsonify({'message:': 'Success'}), 200