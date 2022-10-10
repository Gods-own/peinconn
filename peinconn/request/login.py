from flask import request, jsonify, make_response

def login_request():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Username is required'}), 400)
    if not password:
        return make_response(jsonify({'success': False, 'code': 400, 'message': 'Password is required'}), 400)

    return True  