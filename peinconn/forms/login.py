from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, RadioField, SelectField, PasswordField, validators
import email_validator
from wtforms import ValidationError
from ..models import User
from werkzeug.security import check_password_hash, generate_password_hash

def userExists(tb_name, tb_column):
    message = f'User does not exists'

    def _userExists(form, field):
        tb_filter = {tb_column: field.data}
        the_model_field = tb_name.query.filter_by(**tb_filter).first()
        if the_model_field is None:
            raise ValidationError(message)
    return _userExists

class LoginForm(FlaskForm):   
    username = StringField('Username', [validators.DataRequired(), userExists(User, 'username')]) 
    password = PasswordField('Password', [validators.DataRequired()])  