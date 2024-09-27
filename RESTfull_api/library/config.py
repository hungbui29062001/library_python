import os
from dotenv import load_dotenv
from flask import current_app

load_dotenv()
SECRET_KEY = os.environ.get("KEY")
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
FLASK_SQLALCHEMY_ECHO=True
FLASK_DEBUG=os.environ.get("FLASK_DEBUG")
UPLOAD_FOLDER=os.environ.get('UPLOAD_FOLDER')