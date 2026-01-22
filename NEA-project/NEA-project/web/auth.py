from flask import Blueprint, request, flash, render_template, url_for, redirect
from .models import User,Item
from werkzeug.security import generate_password_hash,check_password_hash
auth = Blueprint("auth", __name__)
# imports the db from _init_.py
from . import db 
from flask_login import login_user,login_required,logout_user,current_user

@auth.route("/login",methods=["GET","POST"]) 
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("logged in successfully", category="success")
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
            flash("Account created", category="success")
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

@auth.route("/items", methods=["GET"])
def items():
    items = Item.query.all()
    return render_template("items.html", items=items)

@auth.route("/items/<int:id>/delete", methods=["POST"])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash("item deleted" , category="success")
    return redirect(url_for("views.items"))

@auth.route("/items/<int:id>/edit", methods=["GET", "POST"])
def edit_item(id):
    item = Item.query.get_or_404(id)

    if request.method == "POST":
        item.name = request.form["name"]
        item.stock = request.form["stock"]
        db.session.commit()
        flash("Item editted", category="success")    
    return redirect(url_for("views.items"))

    

@auth.route("/items/add", methods=["POST"])
def add_item():
    item = Item(
        name=request.form["name"],
        stock=request.form["stock"]
    )
    db.session.add(item)
    db.session.commit()
    flash("item created successfuly", category="success")
    return redirect(url_for("views.view_item", item_id=item.id))



