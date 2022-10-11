from flask import request, jsonify, make_response, current_app
from flask_restful import Resource
from peinconn.peinconn.extensions import db
from peinconn.peinconn.transformers import activity_schema
from peinconn.peinconn.models import Activity as UserActivity, Interest, User
from peinconn.peinconn.helpers.utils import save_file, remove_file
from peinconn.peinconn.request.activity import activity_request
from peinconn.peinconn.helpers.jwt_auth import token_required, get_current_user


class Activity(Resource):

    @token_required
    def get(self, activity_id):

        try:

            print(activity_id)

            activity = UserActivity.query.filter_by(id = activity_id).one()

            activityTransformer = activity_schema.dump(activity)

            url_tupple = (current_app.config['APP_URL'], 'static', activityTransformer['picture'] )

            activityTransformer['picture'] = "/".join(url_tupple)

            return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Activity Successfully', 'data': activityTransformer}) 
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': e.code , 'message': str(e)}), e.code)

    @token_required
    def put(self, activity_id):

        try:
            activity_values_validation = activity_request()

            if activity_values_validation == True:

                activity_model = UserActivity.query.filter_by(id = activity_id).one()

                activity = request.form.get('activity')
                raw_picture = request.files['picture']
                interest_id = request.form.get('interest_id')

                interest = db.session.query(Interest).filter_by(id = interest_id).one()

                file_name = raw_picture.filename
                
                remove_file(activity_model.picture)

                picture = save_file(raw_picture, file_name)

                activity_model.activity = request.form.get('activity')
                activity_model.picture = picture
                activity_model.interest = interest

                db.session.commit()

                return make_response(jsonify({'success': True, 'code': 200, 'message': 'Activity Updated Successfully'}), 201)
            else:
                return activity_values_validation     
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)

class ActivityList(Resource):
    @token_required
    def post(self):

        # try:
        activity_values_validation = activity_request()

        if activity_values_validation == True:

            auth_user = get_current_user()

            user = User.query.filter_by(id=auth_user['id']).one()

            activity = request.form.get('activity')
            raw_picture = request.files['picture']
            interest_id = request.form.get('interest_id')
            like_no = 0

            interest = db.session.query(Interest).filter_by(id = interest_id).one()

            file_name = raw_picture.filename

            picture = save_file(raw_picture, file_name)

            new_activity = Activity(user=user, activity=activity, picture=picture, interest=interest, like_no=like_no)

            db.session.add(new_activity)
            db.session.commit()

            activityTransformer = activity_schema.dump(new_activity)

            return jsonify({'success': True, 'code': 200, 'message': 'Activity added Successfully', 'data': activityTransformer})
        else:
            return activity_values_validation     
        # except Exception as e:
        #     print(e)
        #     return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)    
        

class UserActivities(Resource):
    @token_required
    def get(self):

        try:

            auth_user = get_current_user()

            user_activities = UserActivity.query.filter_by(user_id=auth_user['id']).one()

            activityTransformer = activity_schema.dump(user_activities)

            return jsonify({'success': True, 'code': 200, 'message': 'Activity added Successfully', 'data': activityTransformer})
  
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)    
               