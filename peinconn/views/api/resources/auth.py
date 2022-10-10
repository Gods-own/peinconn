from flask import request, jsonify, session, current_app, make_response
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import datetime
from flask_restful import Resource
from peinconn.peinconn.extensions import db
from peinconn.peinconn.transformers import user_schema
from peinconn.peinconn.models import User, Country
from peinconn.peinconn.request.login import login_request
from peinconn.peinconn.request.register import registration_request

class Login(Resource):
    def post(self):

        try:
            login_values_validation = login_request()
            if login_values_validation == True:
                user_model = User.query.filter_by(username=request.form['username']).first()

                if not check_password_hash(user_model.password, request.form['password']):
                    return make_response(jsonify({'success': False, 'code': 400, 'message': 'password incorrect'}), 400) 
                else:
                    userTransformer = user_schema.dump(user_model)
                    secret = current_app.config["SECRET_KEY"]
                    token = jwt.encode({
                        'id': user_model.id,
                        'username': user_model.username,
                        'email': user_model.email,
                        'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=1)
                    }, secret, algorithm="HS256")

                    token_decoded = token.decode('UTF-8')

                    return jsonify({'success': True, 'code': 200, 'message': 'Login Successful', 'data': {'bearer_token': token_decoded, 'user': userTransformer}})
            else:
                return login_values_validation     
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)         

class Register(Resource):
    def post(self):

        try:
  
            register_values_validation = registration_request()

            if register_values_validation == True:

                password = generate_password_hash(request.form['password'])

                country_model = Country.query.filter_by(id=request.form['country_id']).first()

                dateofbirth_list = request.form['date_of_birth'].split("-")

                date_of_birth = datetime.date(int(dateofbirth_list[0]), int(dateofbirth_list[1]), int(dateofbirth_list[2]))

                user = User(username=request.form['username'], name=request.form['name'], email=request.form['email'], country=country_model, password=password, gender=request.form['gender'], date_of_birth=date_of_birth)
                db.session.add(user)
                db.session.commit()

                userTransformer = user_schema.dump(user)
                secret = current_app.config["SECRET_KEY"]
                token = jwt.encode({
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=1)
                }, secret, algorithm="HS256")

                token_decoded = token.decode('UTF-8')

                return jsonify({'success': True, 'code': 200, 'message': 'Registration Successful', 'data': {'bearer_token': token_decoded, 'user': userTransformer}})
            else:
                return register_values_validation   
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)              


