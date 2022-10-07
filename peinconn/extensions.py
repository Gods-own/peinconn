from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
api = Api()