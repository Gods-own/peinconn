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

interests = db.Table('interests',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('interest_id', db.Integer, db.ForeignKey('interest.id'), primary_key=True))

class Country(CommonField):
    country_abbrev = db.Column(db.String(3), unique=True, nullable=False)
    country = db.Column(db.String(80), unique=True, nullable=False)  

    def __init__(self, country_abbrev, country):
        self.country_abbrev = country_abbrev
        self.country = country

class User(CommonField):
    
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
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
    interests = db.relationship('Interest', secondary=interests, lazy='subquery',
        backref=db.backref('interest_users', lazy=True))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id', ondelete='CASCADE'), nullable=False)    
    country = db.relationship('Country', backref=db.backref('country_users', lazy=True), lazy=True)    

    def __repr__(self):
        return '<User %r>' % self.username

class Interest(CommonField):
    hobby = db.Column(db.String(80), unique=True, nullable=False) 
    hobby_image = db.Column(db.String, nullable=False)

    def __init__(self, hobby, hobby_image):
        self.hobby = hobby
        self.hobby_image = hobby_image

class Activity(CommonField):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    user = db.relationship('User', backref=db.backref('activity_users', lazy=True), lazy=True) 
    activity = db.Column(db.Text, nullable=True)
    picture = db.Column(db.String, nullable=True)
    interest_id = db.Column(db.Integer, db.ForeignKey('interest.id'),
        nullable=False) 
    interest = db.relationship('Interest', backref=db.backref('activities_interests', lazy=True), lazy=True)    
    like_no = db.Column(db.Integer, default=0)

    def __init__(self, user_id, activity, picture, like_no, interest):
        self.user_id = user_id
        self.activity = activity
        self.picture = picture
        # self.interest_id = interest_id
        self.like_no = like_no
        self.interest = interest

class Liked(CommonField):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    user = db.relationship('User', backref=db.backref('liked_users', lazy=True), lazy=True)         
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'),
        nullable=False)
    activity = db.relationship('Activity', backref=db.backref('liked_activities', lazy=True), lazy=True)         
    is_liked = db.Column(db.SmallInteger, default=0, nullable=False)


