from flask import Flask, request, jsonify
from .extensions import db, migrate, api
from .views.web import web
from .views.api import api_bp
import os  

def create_app():
    app = Flask(__name__)

    app.config.from_object("config.DevelopmentConfig")

    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(web) 

    app.register_blueprint(api_bp)

    return app
   
 



