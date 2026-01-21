from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
Db_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'wesfsfsd3323d'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{Db_NAME}"
    db.init_app(app)
    from .auth import auth
    from .views import views
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User,Item
   
    with app.app_context():
        db.create_all()

    return app

def create_database(app):
    if not path.exists("website/" + Db_NAME):
        db.create_all(app = app)
        print("Database Created")