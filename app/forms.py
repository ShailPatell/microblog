from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired


#This will be the Login Form for our blog

class LoginForm(FlaskForm):
    #Create our usernames, passwords, etc., using the four classes we have imported from WTFORMS.
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')