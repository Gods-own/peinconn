from flask import request, jsonify, session
from flask_restful import Api, Resource, reqparse
from peinconn.peinconn.extensions import db
from peinconn.peinconn.transformers import ActivitySchema, activity_schema, InterestSchema, interest_schema
from peinconn.peinconn.models import Activity, Interest
from peinconn.peinconn.helpers.utils import save_file

class ActivityList(Resource):
    def post(self):
        user_id = 1
        activity = request.form.get('activity')
        raw_picture = request.files['picture']
        interest_id = request.form.get('interest_id')
        like_no = 0

        get_interest = db.session.query(Interest).filter_by(id = interest_id).one()

        result = interest_schema.dump(get_interest)

        # interest = get_interest

        # # print(result)

        # # return jsonify(result)

        file_name = raw_picture.filename

        picture = save_file(raw_picture, file_name)

        # # result.pop('id')
        # # result.pop('created_At')
        # # result.pop('updated_At')

        # old_interest = Interest(**result)

        new_activity = Activity(user_id=user_id, activity=activity, picture=picture, interest=get_interest, like_no=like_no)

        print(new_activity)

        db.session.add(new_activity)
        db.session.commit()

        # new_activity.interestt = result


        return activity_schema.dump(new_activity)


        # if 'image_post' not in request.files:
        #     return jsonify({'data': data, 'message': 'Image required'})
        # else:
        #     return jsonify({'data': data, 'message': 'bad'})  
        