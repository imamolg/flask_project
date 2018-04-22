# all the imports
from flask import Flask, render_template,request,redirect,url_for,session, flash
import sys
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
# from config import BaseConfig
# import sqlite3
from flask_bcrypt import Bcrypt

# print('This error output', file=sys.stderr)
app= Flask(__name__)
bcrypt = Bcrypt(app)
# app.secret_key="goirhorjh7569379"
# app.config['SQLALCHEMY_DATABASE_URI']= r'sqlite:///C:\Users\Chetan Baadkar\Documents\GitHub\flask_project\posts2.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config.from_object('config.DevelopmentConfig')
import os
# app.config.from_object('APP_SETTINGS')
# C:\Users\Chetan Baadkar\Documents\GitHub\flask_project
# app.database = "sample.db"

#create sqlalchemy object
db = SQLAlchemy(app)
from .models import BlogPosts

#login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():
    """
    Render a Hello World response.
    :return: Flask response
    """
    # g.db = connect_db()
    # # db = connect_db()
    # # cursor = db.cursor()
    # cur = g.db.execute('select * from posts')
    # # cursor.execute('select * from posts')
    posts = db.session.query(BlogPosts).all()
    # posts = [dict(title=row[1],description=row[2]) for row in cur.fetchall()]
    # g.db.close()
    # # cursor.close()

    return render_template('index.html', posts= posts)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    print('startpoint', file=sys.stderr)
    if request.method =="POST":
        print('this is A', file=sys.stderr)
        if request.form['username']!='admin' or request.form['password']!= 'admin':
            error = 'Invalid credentials.Please try again.'
        else:
            session['logged_in'] = True
            flash('You are now logged in!')
            return redirect(url_for('home'))
    return render_template('login.html',error =error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in',None)
    flash('You are now logged out!')
    return redirect(url_for('welcome'))




# def connect_db():
#     return sqlite3.connect(app.database)
