# all the imports
from flask import Flask, render_template

app= Flask(__name__)


@app.route('/')
def home():
    """
    Render a Hello World response.
    :return: Flask response
    """
    return 'Hello World!'


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

# @app.route('/login',methods=['GET','POST'])
# def login():
#     error = None
#     if request.form=='POST':
#         if reuest.form[username]!='admin'
#     return render_template('login.html',error =error)
