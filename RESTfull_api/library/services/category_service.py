from library.extension import db
from library.library_ma import CategorySchema
from library.models.category import Category
from flask import request, jsonify

category_schema = CategorySchema()
categorys_schema = CategorySchema(many=True)

def add_category_service():
    name = request.json['name']

    try:
        new_category = Category(name)
        db.session.add(new_category)
        db.session.commit()
        return category_schema.jsonify(new_category), 200
    except IndentationError:
        db.session.rollback()
        return jsonify({'message:': 'Add failed'}), 500