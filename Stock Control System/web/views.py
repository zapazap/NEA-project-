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
    return render_template("home.html")

@views.route("/business1") 
def business1():
    return render_template("business1.html")

@views.route("/business2") 
def business2():
    return render_template("business2.html")

@views.route("/business3") 
def business3():
    return render_template("business3.html")

@views.route("/createGroup") 
def createGroup():
    group = Group.query.all()
    return render_template("createGroup.html", groups=len(group))

@views.route("group/<int:group_id>") 
def group(group_id):
    details = Item.query.filter_by(group_id=group_id) 
    return render_template("group.html", details = details)

