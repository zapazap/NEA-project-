from flask import Blueprint, render_template
views = Blueprint("views", __name__)
from flask_login import login_required,current_user

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