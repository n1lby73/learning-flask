from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class regForm (FlaskForm):
    
    username = StringField('Username', validators=[InputRequired(), Length(min=5, max=20, message='username must be between 5-20 characters')])

    email = EmailField('Email', validators=[InputRequired(), Email('Input a valid email')]) 

    password = PasswordField("Password", validators=[InputRequired(), EqualTo("confirmpass",message="Password must be the same"), Length(min=8, max=20, message='Password must be  between 8-20 characters')])

    confirmpass = PasswordField("Confirm password", validators=[InputRequired(), EqualTo('password', message="Password must be same")])

    reg = SubmitField("Sign up")
