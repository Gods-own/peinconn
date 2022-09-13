from flask import Flask, request, jsonify
from .extensions import db, migrate
from .views.web import web
import os  

def create_app():
    app = Flask(__name__)

    app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(web) 

    return app
   
 



