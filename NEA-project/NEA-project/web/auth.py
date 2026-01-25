from flask import Blueprint, request, flash, render_template, url_for, redirect
from .models import User,Item
from werkzeug.security import generate_password_hash,check_password_hash
auth = Blueprint("auth", __name__)
# imports the db from _init_.py
from . import db 
from flask_login import login_user,login_required,logout_user,current_user
import datetime
from sqlalchemy import update
@auth.route("/login",methods=["GET","POST"]) 
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user,remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("incorrect password", category="error")
        else:
            flash("user does not exist", category="error")
        
        return redirect(url_for("views.login"))


@auth.route("/register",methods=["GET" ,"POST"]) 
def register():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        user = User.query.filter_by(email=email).first()

        if user:
            flash("user already exists", category="error")
        elif len(email) < 4:
            flash("Email must be greater than four characters", category="error")

        elif len(first_name) < 2:
            flash("First name too short", category="error")

        elif len(password1) < 7:
            flash("Password too short", category="error")

        elif password1 != password2:
            flash("Passwords do not match", category="error")
        else:
            # add user to database here
            new_user = User(email = email, first_name = first_name, password=generate_password_hash(password1) )
            db.session.add(new_user)
            db.session.commit()
            login_user(user,remember=True)
            return redirect(url_for("views.register"))
        return render_template("register.html")

@auth.route("/resetPassword",methods=["GET","POST"]) 
def resetPassword():
    return redirect(url_for("views.resetPassword"))

@auth.route("/logout") 
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.login"))



@auth.route("/group1", methods = ["POST"])
def addItem():
    id = request.form.get("ID")
    item_edit = request.form.get("item_edit")
    print(id,item_edit)
    if id != None:
        Item.query.filter_by(id=id).delete()
    elif item_edit != None:
        id = request.form.get("id_edit")
        name = request.form.get("item_edit")
        print("Hello world")
        stock = request.form.get("stock_edit")
        price = request.form.get("price_edit")
        Item.query.filter_by(id=id).update({"name":name,"stock":stock,"price":price})
        db.session.commit()

    else:
        name = request.form.get("name")
        stock = request.form.get("stock")
        price = request.form.get("price")
        date=datetime.date.today()
        if int(stock) < 0:
            flash("stock cannot be less than zero.",category="error")
            return redirect(url_for("views.group1"))
        new_item = Item( name = name, stock = stock, price = price, date = date )
        db.session.add(new_item)
    db.session.commit()
    return redirect(url_for("views.group1"))
    

