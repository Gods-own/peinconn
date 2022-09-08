from flask import Flask, request, jsonify
from .extensions import db
import os

def create_app():
    app = Flask(__name__)

    app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)

    return app

from peinconn import views


