from flask import Blueprint, request, flash, render_template, url_for, redirect
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
auth = Blueprint("auth", __name__)

@auth.route("/login",methods=["GET","POST"]) 
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
    return render_template(url_for("views.login"))


@auth.route("/register",methods=["POST"]) 
def register():
    if request.method == "POST":
        first_name = request.form.get("firstname")
        last_name = request.form.get("lastname")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        if len(email) < 4:
            flash("Email must be greater than four characters", category="error")

        elif len(first_name) < 2:
            flash("First name too short", category="error")
        
        elif len(last_name) < 2:
            flash("last name too short", category="error")

        elif len(password1) < 7:
            flash("Password too short", category="error")

        elif password1 != password2:
            flash("Passwords do not match", category="error")
        else:
            # add user to database here
            new_user = User(email = email, first_name = first_name, last_name = last_name, password=generate_password_hash(password1) )
            db.session.add(new_user)
            db.session.commit()
            flash("Account created", category="success")
            return redirect(url_for("views.home"))
        return render_template("register.html")

@auth.route("/resetPassword",methods=["POST"]) 
def resetPassword():
    return render_template(url_for("views.resetPassword"))
    