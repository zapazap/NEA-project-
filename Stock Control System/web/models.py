from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500))
    first_name = db.Column(db.String(50))
    business_id = db.Column(db.Integer, ForeignKey("business.id"))
    business = db.relationship("Business")

class Business(db.Model):
    __tablename__ = "business"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    

class Group(db.Model):
    __tablename__ = "group"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    business_id = db.Column(db.Integer, ForeignKey("business.id"),primary_key=True)
    business = db.relationship("Business")

class Item(db.Model):
    __tablename__ = "item"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    stock = db.Column(db.Integer, default = 0)
    price = db.Column(db.Integer)
    date = db.Column(db.String(20))
    group_id = db.Column(db.Integer, ForeignKey("group.id"),primary_key=True) 
    group = db.relationship("Group")

