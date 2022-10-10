from flask import request, jsonify, make_response
from peinconn.peinconn.models import User
from peinconn.peinconn.helpers.jwt_auth import get_current_user

def interest_register_request():
    interests = request.form.getlist('interests')

    user = get_current_user()

    user_model = User.query.filter(User.interests.any(id=user['id'])).all()

    user_interests = user_model[0].interests

    # hhh = User.query.filter(User.interests.any(id=session['user_id'])).all()

    if len(user_interests) >= 2:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'User already added two interests'}), 400)
    if not interests:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Interests is required'}), 400)
    if len(interests) <= 0:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Please pick at least one interests'}), 400)
    if len(user_interests) == 1 and len(interests) > 1:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Please pick one interests'}), 400)
    if len(interests) > 2:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Please pick at most two interests'}), 400)     

    return True  