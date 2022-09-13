from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, RadioField, SelectField, PasswordField, validators
from country_list import countries_for_language
import email_validator
from ..extensions import db
from sqlalchemy.sql import exists
countries = dict(countries_for_language('en'))

print(db.session)

def uniqueColumn(tb_name, tb_column):
    message = f'already exists'

    def _uniqueColumn(form, field):
        is_data_exists = db.session.query(db.exists().where(tb_name.tb_column == field.data))
        if is_data_exists == True:
            raise ValidationError(message)

    return _uniqueColumn     

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[validators.DataRequired()])      
    username = StringField('Username', validators=[validators.DataRequired(), uniqueColumn(User, username)]) 
    email = StringField('Email', validators=[validators.DataRequired(), validators.Email(message="Email format not correct")])    
    date_of_birth = DateField('Date of Birth', validators=[validators.DataRequired()])
    gender = RadioField('Gender', validators=[validators.DataRequired()], choices=[('male', 'Male'), ('female', 'Female')])
    country = SelectField('Country', validators=[validators.DataRequired(), uniqueColumn(Country, country)], choices=[item for item in countries.items()])
    password = PasswordField('Password', validators=[validators.DataRequired(), validators.EqualTo('password_confirmation', message='Passwords must match')])  
    password_confirmation = PasswordField('Confirm password', validators=[validators.DataRequired()])