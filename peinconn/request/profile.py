from flask import request, jsonify, make_response
from peinconn.peinconn.extensions import db
from peinconn.peinconn.models import User
from peinconn.peinconn.helpers.jwt_auth import get_current_user
from peinconn.peinconn.helpers.utils import uniqueColumn

def profile_update_request():
    username = request.form.get('username')
    name = request.form.get('name')
    userImage = request.files['userImage']
    introduction = request.form.get('introduction')

    if not username:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Username is required'}), 400)

    is_username_unique = uniqueColumn(User.username, 'User', username)   

    if is_username_unique is not True:
        return is_username_unique
        
    if not name:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Name is required'}), 400)
    if not userImage:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'User Image is required'}), 400)
    if not introduction:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Introduction is required'}), 400) 
    return True 