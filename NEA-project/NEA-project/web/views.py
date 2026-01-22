from flask import Blueprint, render_template
views = Blueprint("views", __name__)
from flask_login import login_required,current_user
from . import db
from .models import Item

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
    return render_template("createGroup.html")

@views.route("/group1") 
def group1():
    return render_template("group1.html")

@views.route("/items/<int:id>/edit")
def edit_item(id):
    item = Item.query.get_or_404(id)
    return render_template("edit_item.html", item=item)

@views.route("/items/<int:item_id>")
def view_item(item_id):
    item = Item.query.get_or_404(item_id)
    return render_template("item.html", item=item)