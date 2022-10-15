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

    # def __init__(self, country_abbrev, country):
    #     self.country_abbrev = country_abbrev
    #     self.country = country

class Activity(CommonField):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    user = db.relationship('User', back_populates="activities", lazy=True) 
    activity = db.Column(db.Text, nullable=True)
    picture = db.Column(db.String, nullable=True)
    interest_id = db.Column(db.Integer, db.ForeignKey('interest.id'),
        nullable=False) 
    interest = db.relationship('Interest', backref=db.backref('activities_interests', lazy=True), lazy=True)    
    like_no = db.Column(db.Integer, default=0)


class User(CommonField):  
    
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    introduction = db.Column(db.Text, nullable=True)
    gender = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    userImage = db.Column(db.String, default="default-image.png")
    is_admin = db.Column(db.SmallInteger, default=0)
    is_active = db.Column(db.SmallInteger, default=1, nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_login = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    interests = db.relationship('Interest', secondary=interests, lazy='subquery',
        backref=db.backref('interest_users', lazy=True))
    activities = db.relationship('Activity', back_populates="user", lazy=True)     
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)    
    country = db.relationship('Country', backref=db.backref('country_users', lazy=True), lazy=True)    

    def __repr__(self):
        return '<User %r>' % self.username
  
    # def __init__(self, username, name, email, password, introduction, gender, date_of_birth, user_image, is_admin, 
    #     country):
    #     self.username = username
    #     self.name = name
    #     self.email = email
    #     self.password = password
    #     self.introduction = introduction
    #     self.gender = gender
    #     self.date_of_birth = date_of_birth
    #     self.is_admin = is_admin
    #     self.interests = interests
    #     self.country = country  

class Interest(CommonField):
    hobby = db.Column(db.String(80), unique=True, nullable=False) 
    hobby_image = db.Column(db.String, nullable=False)

    def __init__(self, hobby, hobby_image):
        self.hobby = hobby
        self.hobby_image = hobby_image

    # def __init__(self, user, activity, picture, like_no, interest):
    #     self.user = user
    #     self.activity = activity
    #     self.picture = picture
    #     # self.interest_id = interest_id
    #     self.like_no = like_no
    #     self.interest = interest

class Liked(CommonField):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'),
        nullable=False)
    user = db.relationship('User', back_populates='liked_users', lazy=True)         
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id', ondelete='CASCADE'),
        nullable=False)
    activity = db.relationship('Activity', back_populates='liked_activities', lazy=True)         
    is_liked = db.Column(db.SmallInteger, default=0, nullable=False)

class Room(CommonField):
    room = db.Column(db.String(225), nullable=False)
    user1_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user1 = db.relationship('User', back_populates="chatter1", lazy=True)
    user2_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user2 = db.relationship('User', back_populates="chatter2", lazy=True)

class Message(CommonField):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates="sender", lazy=True) 
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    room = db.relationship('Room', back_populates="dm_room", lazy=True) 
    content = db.Column(db.Text, nullable=False)

class Notifications(CommonField):
    notification_user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    notification_user = db.relationship('User', back_populates="sent_to", lazy=True)
    notification_message_id =  db.Column(db.Integer, db.ForeignKey('message.id', ondelete='CASCADE'), nullable=False)
    notification_message = db.relationship('Message', back_populates="new_message", lazy=True)
    notification_read = db.Column(db.SmallInteger, default=0, nullable=False)

class Connected(CommonField):
    connected_user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    connected_user = db.relationship('User', back_populates="connected_user", lazy=True) 
    connection_room_id = db.Column(db.Integer, db.ForeignKey('room.id', ondelete='CASCADE'), nullable=False)
    connection_room = db.relationship('Room', back_populates="connected_room", lazy=True) 
    channel_name = db.Column(db.Text, nullable=False)   



