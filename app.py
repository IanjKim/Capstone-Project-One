from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet

CURRENT_USER_KEY = "current_user"

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///dog-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True

connect_db(app)



@app.route("/")
def homepage():
    """Home page"""

    return "ian"