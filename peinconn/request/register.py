from flask import request, jsonify, make_response

def registration_request():
    username = request.form.get('username')
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    gender = request.form.get('gender')
    date_of_birth = request.form.get('date_of_birth')
    country_id = request.form.get('country_id')

    if not username:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Username is required'}), 400)
    if not name:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Name is required'}), 400)
    if not email:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Email is required'}), 400)
    if not password:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Password is required'}), 400)
    if not gender:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Gender is required'}), 400)
    if not date_of_birth:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Date of birth is required'}), 400)
    if not country_id:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Country ID is required'}), 400)  
    return True                              