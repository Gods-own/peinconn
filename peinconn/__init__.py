from flask import Flask, request, jsonify
from .extensions import db, ma, migrate, api, seeder, socketio
from .views.web import web
from .views.api import api_bp
from peinconn import config

def create_app():
    app = Flask(__name__)

    app.config.from_object(config.DevelopmentConfig)

    socketio.init_app(app, manage_session=False)
    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    seeder.init_app(app, db)
    migrate.init_app(app, db)

    app.register_blueprint(web) 

    app.register_blueprint(api_bp)

    return app
   
 



