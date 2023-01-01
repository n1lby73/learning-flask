from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class regForm (FlaskForm):

    username = StringField('username', validators=[InputRequired(), Length(min=5, max=20, message='username must be between 5-20 characters')])

    email = EmailField('email', validators=[InputRequired(), Email('Input a valid email')]) 

    password = PasswordField("password", validators=[InputRequired(), EqualTo("confirmpass",message="password must be the same"), Length(min=8, max=20, message='password must be  between 8-20 characters')])

    confirmpass = PasswordField("Confirm password", validators=[InputRequired(), EqualTo('password', message="passwords must be same")])

    reg = SubmitField("sign up")
