from flask import request, jsonify, make_response, current_app, url_for
from flask_restful import Resource
from peinconn.peinconn.extensions import db
from peinconn.peinconn.transformers import ActivitySchema, activity_schema, activities_schema
from peinconn.peinconn.models import Activity as UserActivity, Interest, User, Liked
from peinconn.peinconn.helpers.utils import save_file, remove_file, get_file_url
from peinconn.peinconn.helpers.pagination import get_pagination
from peinconn.peinconn.request.activity import activity_request
from peinconn.peinconn.helpers.jwt_auth import token_required, get_current_user


class LikeActivity(Resource):

    @token_required
    def get(self, activity_id):

        try:
            auth_user = get_current_user()

            liked_model = Liked.query.filter_by( user_id = auth_user['id'], activity_id = activity_id).first()

            if liked_model is None:

                return jsonify({'success': True, 'code': 200, 'message': 'Liked Status Retrieved Succcessfully', 'data': {'is_liked': False}}) 
            else:
                if liked_model.is_liked == False:
                    return jsonify({'success': True, 'code': 200, 'message': 'Liked Status Retrieved Succcessfully', 'data': {'is_liked': False}}) 
                elif liked_model.is_liked == True:        
                    return jsonify({'success': True, 'code': 200, 'message': 'Liked Status Retrieved Succcessfully', 'data': {'is_liked': True}}) 
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)

    @token_required
    def put(self, activity_id):

        try:

            auth_user = get_current_user()

            activity_model = UserActivity.query.filter_by(id = activity_id).one()

            liked_model = Liked.query.filter_by( user_id = auth_user['id'], activity_id = activity_id).first()

            if liked_model is None:

                new_liked = Liked(user_id=auth_user['id'], activity_id=activity_id, is_liked=True)

                activity_model.like_no = activity_model.like_no + 1

                db.session.add(new_liked)
                db.session.commit()

                return make_response(jsonify({'success': True, 'code': 200, 'message': 'Activity Liked Successfully'}), 200)

            else:

                if liked_model.is_liked == False:

                    activity_model.like_no = activity_model.like_no + 1
                    liked_model.is_liked = True

                    db.session.commit()   

                    return make_response(jsonify({'success': True, 'code': 200, 'message': 'Activity Liked Successfully'}), 200) 

                elif liked_model.is_liked == True:  
                    activity_model.like_no = activity_model.like_no - 1
                    liked_model.is_liked = False

                    db.session.commit()   

                    return make_response(jsonify({'success': True, 'code': 200, 'message': 'Activity Unliked Successfully'}), 200)   

                return make_response(jsonify({'success': True, 'code': 200, 'message': 'Activity Updated Successfully'}), 201)

        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)
