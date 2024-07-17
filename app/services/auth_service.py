from functools import wraps
from flask import request, jsonify, current_app
from app.models import User

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key != current_app.config['ADMIN_API_KEY']:
            return jsonify({'error': 'Unauthorized access'}), 401
        return f(*args, **kwargs)
    return decorated_function

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_token = request.headers.get('Authorization')
        if not auth_token:
            return jsonify({'error': 'Authorization token required'}), 401
        # Implement token validation logic here
        return f(*args, **kwargs)
    return decorated_function
