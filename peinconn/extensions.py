from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_seeder import FlaskSeeder

db = SQLAlchemy()
seeder = FlaskSeeder()
ma = Marshmallow()
migrate = Migrate()
api = Api()