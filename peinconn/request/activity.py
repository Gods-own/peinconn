from flask import request, jsonify, make_response
from peinconn.peinconn.models import User, Interest, Activity
from peinconn.peinconn.helpers.jwt_auth import get_current_user

def activity_request():
    activity = request.form.get('activity')
    interest_id = request.form.get('interest_id')
    picture = request.files['picture']

    user = get_current_user()

    user_model = User.query.filter(User.interests.any(User.id==user['id'])).all()

    # hhh = User.query.filter(User.interests.any(id=session['user_id'])).all()

    if not activity:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Activity is required'}), 400)
    if not interest_id:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Interest Id is required'}), 400)
    if not picture:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Picture is required'}), 400) 
    if len(user_model) != 0:     
        user_interests = user_model[0].interests

        user_interests_id = [user_interest.id for user_interest in user_interests]

        if int(interest_id) not in user_interests_id:        
            return make_response(jsonify({'success': False, 'code': 400, 'message': 'User does not have this Interest'}), 400)       

    return True  