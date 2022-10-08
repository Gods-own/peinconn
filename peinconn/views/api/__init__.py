from flask import Blueprint
from flask_restful import Api, Resource, url_for
from peinconn.peinconn.views.api.resources.activity import ActivityList

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(api_bp)

api.add_resource(ActivityList, '/activities')

