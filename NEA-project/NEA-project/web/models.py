from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id=db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    Item = db.Relationship("Item")

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.String(30))
    item__count = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))