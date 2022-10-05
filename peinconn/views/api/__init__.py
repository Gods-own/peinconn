from flask import Blueprint
from flask_restful import Api, Resource, url_for

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(api_bp)

