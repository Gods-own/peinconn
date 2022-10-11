from flask import request, jsonify, make_response, current_app
from flask_restful import Resource
from peinconn.peinconn.extensions import db
from peinconn.peinconn.transformers import user_schema, user_details_schema
from peinconn.peinconn.models import User as AuthUser
from peinconn.peinconn.helpers.utils import save_file, remove_file
from peinconn.peinconn.request.profile import profile_update_request
from peinconn.peinconn.helpers.jwt_auth import token_required, get_current_user


class User(Resource):

    @token_required
    def get(self):

        try:

            auth_user = get_current_user()

            user_model = AuthUser.query.filter_by(id=auth_user['id']).one()

            userTransformer = user_schema.dump(user_model)

            url_tupple = (current_app.config['APP_URL'], 'static', userTransformer['userImage'] )

            userTransformer['userImage'] = "/".join(url_tupple)

            return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Activity Successfully', 'data': userTransformer}) 
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)

    @token_required
    def put(self):

        # try:
            profile_values_validation = profile_update_request()

            if profile_values_validation == True:

                auth_user = get_current_user()

                user_model = AuthUser.query.filter_by(id = auth_user['id']).one()

                username = request.form.get('username')
                name = request.form.get('name')
                raw_picture = request.files['userImage']
                introduction = request.form.get('introduction')

                file_name = raw_picture.filename

                print(user_model.userImage != 'default-image.png')

                if user_model.userImage != 'default-image.png':
                
                    remove_file(user_model.userImage)

                picture = save_file(raw_picture, file_name)

                user_model.username = username
                user_model.userImage = picture
                user_model.name = name
                user_model.introduction = introduction

                db.session.commit()

                return make_response(jsonify({'success': True, 'code': 200, 'message': 'Activity Updated Successfully'}), 201)
            else:
                return profile_values_validation     
        # except Exception as e:
        #     return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)

class AllUserDetails(Resource):

    @token_required
    def get(self):

        try:

            auth_user = get_current_user()

            user_model = AuthUser.query.filter_by(id=auth_user['id']).one()

            userTransformer = user_details_schema.dump(user_model)

            url_tupple = (current_app.config['APP_URL'], 'static', userTransformer['userImage'] )

            userTransformer['userImage'] = "/".join(url_tupple)

            return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Activity Successfully', 'data': userTransformer}) 
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)

