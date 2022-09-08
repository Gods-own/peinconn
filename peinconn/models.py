from peinconn import app
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
import os
from .extensions import db
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declared_attr, has_inherited_table
from datetime import datetime

db = SQLAlchemy(app)

ma = Marshmallow(app)

basedir = os.path.abspath(os.path.dirname(__file__))

class TimestampModel(Model):
    @declared_attr
    def createdAt(cls):
        return sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    def updaetdAt(cls):
        return sa.Column(sa.DateTime, onupdate=datetime.utcnow)    

# db = SQLAlchemy(app, model_class=TimestampModel)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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

    def __repr__(self):
        return '<User %r>' % self.username

# class Interests(models.Model):
#     hobbies = models.CharField(max_length=100, unique=True)
#     user_hobby = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="hobbysist")
#     def __str__(self):
#         return f"{self.user_hobby}"

# class Countries(models.Model):
#     country = models.CharField(max_length=100, unique=True, default=None)
#     user_country = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="citizen")
#     def __str__(self):
#         return f"{self.user_country}"


# class Activities(models.Model):
#     poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="poster")
#     activity = models.TextField()
#     picture = models.ImageField(upload_to="img/%y")
#     hobby = models.ForeignKey(Interests, on_delete=models.CASCADE, default=None, related_name="post_hobby")
#     likes = models.IntegerField(default=0)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def serialize(self):
#         return {
#             "id": self.id,
#             "poster": self.poster.username,
#             "posterImage": self.poster.userImage.url,
#             "activity": self.activity,
#             "picture": self.picture.url,
#             "hobby": self.hobby.hobbies,
#             "likes": self.likes,
#             "timestamp": self.timestamp.strftime("%b %d, %Y, %I:%M %p")
#         }

#     @property
#     def picture_url(self):
#         if self.picture and hasattr(self.picture, 'url'):
#             return self.picture_url

# class Liked(models.Model):
#     liker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="post_liker")
#     activity = models.ForeignKey(Activities, on_delete=models.CASCADE, related_name="post")
#     is_liked = models.BooleanField(default=False)

#     def serialize(self):
#         return {
#             "id": self.id,
#             "liker": self.liker.username,
#             "activity": self.activity.activity,
#             "is_liked": self.is_liked
#         }        

