from flask import Flask, request, jsonify
from flask_sqlalchemy import Model
from flask_marshmallow import Marshmallow
import os
from .extensions import db
import sqlalchemy as sa
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))


class CommonField(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_At = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_At = db.Column(db.DateTime, onupdate=datetime.utcnow)    

# db = SQLAlchemy(app, model_class=TimestampModel)

user_hobby = db.Table('user_hobby',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('interest_id', db.Integer, db.ForeignKey('interest.id'), primary_key=True))

class Country(CommonField):
    country = db.Column(db.String(80), unique=True, nullable=False)
    user = db.relationship('User', backref='country', lazy=True)    

class User(CommonField):
    
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = CommonField
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    introduction = db.Column(db.Text, nullable=True)
    gender = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    userImage = db.Column(db.String, default=f"{basedir}/static/images/default/default-image.png")
    is_admin = db.Column(db.SmallInteger, default=0)
    is_active = db.Column(db.SmallInteger, default=1, nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_login = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    interests = db.relationship('Interest', secondary=user_hobby, lazy='subquery',
        backref=db.backref('users', lazy=True))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'),
        nullable=False)    
    activity = db.relationship('Activity', backref='user', lazy=True)     
    liked = db.relationship('Liked', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

class Interest(CommonField):
    hobbies = db.Column(db.String(80), unique=True, nullable=False)
    activity = db.relationship('Activity', backref='interest', lazy=True)


class Activity(CommonField):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    activity = db.Column(db.Text, nullable=True)
    picture = db.Column(db.String, nullable=True)
    interest_id = db.Column(db.Integer, db.ForeignKey('interest.id'),
        nullable=False) 
    like_no = db.Column(db.Integer, default=0)
    liked = db.relationship('Liked', backref='activity', lazy=True)

class Liked(CommonField):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'),
        nullable=False)
    is_liked = db.Column(db.SmallInteger, default=0, nullable=False)


