from flask import Blueprint, render_template
views = Blueprint("views", __name__)
from flask_login import login_required,current_user
from . import db
from .models import *

@views.route("/")
def index():
    return render_template("base.html")

@views.route("/login") 
def login():
    return render_template("login.html")

@views.route("/register") 
def register():
    return render_template("register.html")
    

@views.route("/resetPassword") 
def resetPassword():
    return render_template("resetPassword.html")

@views.route("/home") 
@login_required
def home():
    businesses = Business.query.all()
    return render_template("home.html", businesses=businesses)

@views.route("business/<int:business_id>") 
def business(business_id):
    groups = Group.query.filter_by(business_id=business_id)
    return render_template("business.html", business_id=business_id, groups=groups)

@views.route("/business/<int:business_id>/group/<int:group_id>") 
def group(business_id, group_id):
    details = Item.query.filter_by(group_id=group_id) 
    return render_template("group.html", details=details)

