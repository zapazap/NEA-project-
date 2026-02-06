from flask import Blueprint, request, flash, render_template, url_for, redirect
from .models import *
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
    # requests all inputs from inputboxes in the register page
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        user = User.query.filter_by(email=email).first()        

        # validation for registering username and password
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
            login_user(new_user,remember=True)
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


@auth.route("/business/<int:business_id>", methods = ["POST"])
def addGroup(business_id):  
    name= request.form.get('name')
    id = Group.query.filter_by(business_id=business_id).count()+1
    new_group = Group(id=id, name=name,business_id=business_id)
    db.session.add(new_group)
    db.session.commit()
    return redirect(request.url)


@auth.route("/business/<int:business_id>/group/<int:group_id>", methods = ["POST"])
def addItem(business_id,group_id):  
    id = request.form.get("ID")
    item_edit = request.form.get("item_edit")
    if id != None:
        Item.query.filter_by(id=id, group_id=group_id).delete()
    elif item_edit != None:
        for i in range(len(request.form.getlist("id_edit"))):
            id = request.form.getlist("id_edit")[i]
            name = request.form.getlist("item_edit")[i]
            stock = request.form.getlist("stock_edit")[i]
            price = request.form.getlist("price_edit")[i]
            Item.query.filter_by(id=id, group_id=group_id).update({"name":name,"stock":stock,"price":price})
        db.session.commit()

    else:
        name = request.form.get("name")
        stock = request.form.get("stock")
        price = request.form.get("price")
        date=datetime.date.today()
        if int(stock) < 0:
            flash("stock cannot be less than zero.",category="error")
        elif int(price) < 0:
            flash("price cannot be less than zero.",category="error")
            return redirect(request.url)
        groups = Item.query.filter_by(group_id=group_id)
        new_item = Item(id=groups.count()+1, name=name, stock=stock, price = "£"+price, date = date, group_id = group_id )
        db.session.add(new_item)
    db.session.commit()
    return redirect(request.url)
    

