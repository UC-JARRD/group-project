from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db" #Create a new database from SQLAlchemy



def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = '123456789Q'

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}" #location of the datbase. Store the db in the website folder

    db.init_app(app) #Tell the DB what app to connect to 

    #import the blueprints
    from .views import views
    from .auth import auth

    #register blueprints with flask application
    app.register_blueprint(views, url_prefix = '/')

    #url_prefix will be a root link and will have to be changed in auth.py. 
    app.register_blueprint(auth, url_prefix = '/')

    from .models import User, Note #Make sure the models run before createing a database

    create_database(app)

    return app


def create_database(app):
    if not path.exists(path.join('website', DB_NAME)):
        with app.app_context(): 
            db.create_all()
        print('Created a DB')


