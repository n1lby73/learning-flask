from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class regForm (FlaskForm):

    username = StringField('username')

    email = EmailField('email')

    password = PasswordField("password")

    confirmpass = PasswordField("Confirm password")

    reg = SubmitField("login")
