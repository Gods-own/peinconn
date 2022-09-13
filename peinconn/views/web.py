from flask import Flask, redirect, render_template, request, session, url_for, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from ..forms.register import RegistrationForm
from ..forms.login import LoginForm
from country_list import countries_for_language
from ..models import User, Country
from ..helpers import acc_for_uniqueness, login_required
from ..extensions import db

web = Blueprint('web', __name__)

@web.route('/', methods=['GET', 'POST'])
@login_required
def index():
    # countries = dict(countries_for_language('en'))

    # print([(key, countries[key]) for key in countries.keys()])
    form = RegistrationForm(request.form)
    return render_template("index.html", form=form)

@web.route('/login', methods=['GET', 'POST'])
def login():
    # countries = dict(countries_for_language('en'))

    # print([(key, countries[key]) for key in countries.keys()])
    if request.method == "POST":
        form = LoginForm()

        if form.validate_on_submit():

            the_model_field = User.query.filter_by(username=form.username.data).first()

            if not check_password_hash(the_model_field.password, form.password.data):
                return redirect(url_for('login', message='Incorrect Password'))
            else:

                session["user_id"] = the_model_field.id

                return redirect('/')
        else:    
            return render_template("login.html", form=form)        
    else:    
        form = LoginForm()
        return render_template("login.html", form=form)


@web.route('/register', methods=['GET', 'POST'])
def register():
    # countries = dict(countries_for_language('en'))

    # print([(key, countries[key]) for key in countries.keys()])
    if request.method == "POST":
        form = RegistrationForm()
        print(form.password.data, form.country.data)
        if form.validate_on_submit():
            password = generate_password_hash(form.password.data)

            country = acc_for_uniqueness(Country, {'country': form.country.data}, country=form.country.data)
            print(country)

            user = User(username=form.username.data, name=form.name.data, email=form.email.data, password=password, gender=form.gender.data, date_of_birth=form.date_of_birth.data)
            country.country_users.append(user)
            # country.user = [user]

            # db.session.add(user)
            db.session.add(country)
            db.session.commit()

            return redirect('/')
        else:    
            return render_template("register.html", form=form)
    else:    
        form = RegistrationForm()
        return render_template("register.html", form=form)
