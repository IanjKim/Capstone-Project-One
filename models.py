from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrpyt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """User Table"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True, primary_key=True)
    password = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    
class Breed(db.Model):
    """Breeds Table"""

    __tablename__ = "breeds"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Fact(db.Model):
    """Fact Table"""

    __tablename__ = "facts"

    id = db.Column(db.Integer, primary_key=True)
    breed_id = db.Column(db.Integer, db.ForeignKey('breeds.id'))
    life_span = db.column(db.Integer)