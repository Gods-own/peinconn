import jwt
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        bearer = request.headers.get('Authorization')
        print(bearer)
        return f(^args, **kwargs)
    return decorated_function    