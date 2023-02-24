from flask import Flask, request, redirect, render_template, session, g
from models import db, connect_db, User, Breed, Fact
# from forms import RegisterForm, LoginForm, SearchBreed
import requests

CURRENT_USER_KEY = "current_user"

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///dog-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True

connect_db(app)

@app.before_request
def add_user_to_global():
    """If the user is logged in, add the current user to Flask global."""

    if CURRENT_USER_KEY in session:
        g.user = User.query.get(session[CURRENT_USER_KEY])
    
    else:
        g.user = None
    

def do_login(user):
    """Log in user."""

    session[CURRENT_USER_KEY] = user.id


def do_logout():
    """Log out user."""

    if CURRENT_USER_KEY in session:
        del session[CURRENT_USER_KEY]


@app.route("/")
def homepage():
    """Homepage"""

    return render_template('home.html')

@app.route('/breeds', methods=['GET'])
def show_breeds():
    """Shows list of dog breeds"""

    return render_template('breeds.html')

@app.route('/search', methods=['GET'])
def search_breed():
    """Search for dog breeds"""

    return render_template('search.html')

@app.errorhandler(404)
def page_not_found(error):
    """Error 404 page"""

    return render_template('404.html'), 404
