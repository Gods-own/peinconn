from flask import Blueprint
from .authentication.auth import auth
# from .activity.activity import activity

web = Blueprint('web', __name__)

web.register_blueprint(auth)
# web.register_blueprint(activity)
