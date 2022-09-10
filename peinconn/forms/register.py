from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, RadioField, SelectField, PasswordField, validators
from country_list import countries_for_language
import email_validator
countries = dict(countries_for_language('en'))

print(countries)

class RegistrationForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])      
    username = StringField('Username', [validators.DataRequired()]) 
    email = StringField('email', [validators.DataRequired(), validators.Email(message="Email format not correct")])    
    date_of_birth = DateField('Date of Birth', [validators.DataRequired()])
    gender = RadioField('Gender', [validators.DataRequired()], choices=[('male', 'Male'), ('female', 'Female')])
    country = SelectField('Country', [validators.DataRequired()], choices=[item for item in countries.items()])
    password = PasswordField('Username', [validators.DataRequired(), validators.EqualTo('password_confirmation', message='Passwords must match')])  
    password_confirmation = PasswordField('Username', [validators.DataRequired()])