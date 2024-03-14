from flask import Blueprint
from library.services.auth_service import register_service, login_service, whoami_service, refresh_token_service, logout_service
from flask_jwt_extended import jwt_required

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.post('/register')
def register():
    return register_service()

@auth_bp.post('/login')
def login():
    return login_service()

@auth_bp.get('/whoami')
@jwt_required()
def whoami():
    return whoami_service()

@auth_bp.get('/refresh-token')
@jwt_required(refresh=True)
def refresh_token():
    return refresh_token_service()

@auth_bp.delete('/logout')
@jwt_required(verify_type=False)
def logout():
    return logout_service()