from flask import request, jsonify, session, current_app, make_response
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import datetime
from flask_restful import Api, Resource, reqparse
from peinconn.peinconn.extensions import db
from peinconn.peinconn.models import Interest, User
from peinconn.peinconn.request.interest_register import interest_register_request
from peinconn.peinconn.helpers.jwt_auth import token_required, get_current_user

class RegisterInterest(Resource):
    @token_required
    def post(self):
        try:
            interest_values_validation = interest_register_request()

            if interest_values_validation == True:
                auth_user = get_current_user()

                user = User.query.filter_by(id=auth_user['id']).one()

                # for interest_id in request.form.getlist("interests"):

                #     # interest = acc_for_uniqueness(Interest, {'hobby': data}, hobby=data)
                #     interest_data = db.session.query(Interest).filter_by(id = interest_id).one()

                #     user.interests.append(interest_data)

                # db.session.add(user)
                # db.session.commit()

                # return make_response(jsonify({'success': True, 'code': 200, 'message': 'Added Interests successfully'}), 201)
            else:
                return interest_values_validation     
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)      