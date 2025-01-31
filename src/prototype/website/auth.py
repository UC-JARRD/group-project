from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash #Creates irreversible hashed password that can be used to check on similarity of hash without knowing the password
from . import db   ##means from __init__.py import db


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return render_template("home.html", boolean=True)

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
 
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category = "error") #Use categories to display messages in a different color
        elif len(first_name) < 2:
            flash("First name must be more than 1 character", category = "error")
        elif password1 != password2:
            flash("Passwords don't match", category = "error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters", category = "error")
        else:
            #Create a new user
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='pbkdf2:sha256')) #fields from Models.py
            db.session.add(new_user)
            db.session.commit() #Save changes
            #Add user to the DB
            flash("Account created.", category = "success")
            return redirect(url_for("views.home"))

    return render_template("sign_up.html")