from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500))
    first_name = db.Column(db.String(50))
    item = db.relationship('Item')


class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    stock = db.Column(db.Integer, default = 0)
    price = db.Column(db.Integer)
    date = db.Column(db.String(20))
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))