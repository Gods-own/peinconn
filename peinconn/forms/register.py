from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, RadioField, SelectField, PasswordField, validators
from wtforms import ValidationError
from country_list import countries_for_language
import email_validator
from ..extensions import db
from ..models import User, Country
from sqlalchemy.sql import exists

# countries = dict(countries_for_language('en'))

# def get_countries():
#     with app.app_context():
#         country = Country.query.all()
#         print(country)
#         return country


def uniqueColumn(tb_name, tb_column):
    message = f'{tb_column} already taken'

    def _uniqueColumn(form, field):
        is_data_exists = db.session.query(db.exists().where(tb_name == field.data)).scalar()
        print(is_data_exists)
        if is_data_exists == True:
            raise ValidationError(message)

    return _uniqueColumn     

# def valueExists(tb_name, tb_column):
#     message = f'already exists'

#     def _valueExists(form, field):
#         is_data_exists = db.session.query(db.exists().where(tb_name == field.data)).scalar()
#         print(is_data_exists)
#         if is_data_exists == True:
#             raise ValidationError(message)

#     return _valueExists    

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[validators.DataRequired()])      
    username = StringField('Username', validators=[validators.DataRequired(), uniqueColumn(User.username, 'username')]) 
    email = StringField('Email', validators=[validators.DataRequired(), validators.Email(message="Email format not correct"), uniqueColumn(User.email, 'email')])    
    date_of_birth = DateField('Date of Birth', validators=[validators.DataRequired()])
    gender = RadioField('Gender', validators=[validators.DataRequired()], choices=[('male', 'Male'), ('female', 'Female')])
    country = SelectField('Country', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired(), validators.EqualTo('password_confirmation', message='Passwords must match')])  
    password_confirmation = PasswordField('Confirm password', validators=[validators.DataRequired()])