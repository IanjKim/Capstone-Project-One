from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, InputRequired
from flask_wtf import FlaskForm



class RegisterForm(FlaskForm):
    """User registration form."""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)]
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)]
    )

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField(
        "Username",
        validators=[DataRequired()]
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=8, max=30)]
    )

class SearchBreed(FlaskForm):
    """Breed searching form"""

    breed = StringField(
        "Name of Breed",
        validators=[DataRequired()]
    )