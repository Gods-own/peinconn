from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, RadioField, SelectField, PasswordField, validators
import email_validator

class LoginForm(FlaskForm):   
    username = StringField('Username', [validators.DataRequired()]) 
    password = PasswordField('Password', [validators.DataRequired()])  