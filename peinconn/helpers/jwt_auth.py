from flask import request, jsonify, make_response, current_app
import jwt
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        bearer_token = request.headers.get('Authorization')
        if not bearer_token:
            return make_response(jsonify({'success': False, 'code': 403, 'message': 'Token is required'}), 403) 
        try:
            secret = current_app.config['SECRET_KEY']
            bearer_token= bearer_token.split(" ")
            data = jwt.decode(bearer_token[1], secret, algorithms=["HS256"])    
        except:
            return make_response(jsonify({'success': False, 'code': 403, 'message': 'Token is invalid'}), 403)     
        return f(*args, **kwargs)
    return decorated_function    

def get_current_user():    
    bearer_token = request.headers.get('Authorization')
    if not bearer_token:
        return None
    try:
        secret = current_app.config['SECRET_KEY']
        bearer_token= bearer_token.split(" ")
        data = jwt.decode(bearer_token[1], secret, algorithms=["HS256"]) 
        return data
    except:
        return None    