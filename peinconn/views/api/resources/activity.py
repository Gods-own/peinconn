from flask import request, jsonify
from flask_restful import Api, Resource, reqparse

class ActivityList(Resource):
    def post(self):
        data = request.get_json()
        if 'image_post' not in request.files:
            return jsonify({'data': data, 'message': 'Image required'})
        else:
            return jsonify({'data': data, 'message': 'bad'})  
        