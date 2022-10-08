from flask import Flask, redirect, render_template, request, session, url_for, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from country_list import countries_for_language
from ....helpers import acc_for_uniqueness, login_required, user_already_loggedin, interest_needed
from ....forms.register import RegistrationForm
from ....forms.login import LoginForm
from ....forms.interest import InterestForm
from ....extensions import db
from ....models import User, Country, Interest

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
@user_already_loggedin
def login():
    # countries = dict(countries_for_language('en'))

    # print([(key, countries[key]) for key in countries.keys()])
    if request.method == "POST":
        form = LoginForm()

        if form.validate_on_submit():

            the_model_field = User.query.filter_by(username=form.username.data).first()

            if not check_password_hash(the_model_field.password, form.password.data):
                return render_template("login.html", form=form, message='Incorrect passwordd')    
            else:

                session["user_id"] = the_model_field.id

                return redirect('/')
        else:    
            return render_template("login.html", form=form)        
    else:    
        form = LoginForm()
        return render_template("login.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")

@auth.route('/register', methods=['GET', 'POST'])
@user_already_loggedin
def register():
    country_list = Country.query.all()  
    countries = [(country.id, country.country.capitalize()) for country in country_list]
    form = RegistrationForm()
    form.country.choices = countries
    # countries = dict(countries_for_language('en'))

    # print([(key, countries[key]) for key in countries.keys()])
    if request.method == "POST":
        print(form.password.data, form.country.data)
        if form.validate_on_submit():
            password = generate_password_hash(form.password.data)

            # country = acc_for_uniqueness(Country, {'country': form.country.data}, country=form.country.data)
            # print(country)

            # user = User(username=form.username.data, name=form.name.data, email=form.email.data, password=password, gender=form.gender.data, date_of_birth=form.date_of_birth.data)
            # country.country_users.append(user)
            # country.user = [user]

            # db.session.add(user)
            user = User(username=form.username.data, name=form.name.data, email=form.email.data, country_id=form.country.data, password=password, gender=form.gender.data, date_of_birth=form.date_of_birth.data)
            db.session.add(user)
            db.session.commit()

            session["user_id"] = user.id

            print(session["user_id"])

            return redirect('/add-interests')
        else:    
            return render_template("register.html", form=form)
    else:  
        return render_template("register.html", form=form)

@auth.route('/add-interests', methods=['GET', 'POST'])
@login_required
@interest_needed
def registerInterest():
    # countries = dict(countries_for_language('en'))

    # print([(key, countries[key]) for key in countries.keys()])
    interest_list = Interest.query.all()  
    interests = [(interest.id, interest.hobby.capitalize()) for interest in interest_list]
    form = InterestForm()
    form.interest.choices = interests

    choice_combo = zip(form.interest, interest_list)

    if request.method == "POST":

        if form.validate_on_submit():
            print(form.interest.data)

            user = db.session.query(User).filter_by(id = session['user_id']).one()
            print(user)
            for data in form.interest.data:

                # interest = acc_for_uniqueness(Interest, {'hobby': data}, hobby=data)
                interest_data = db.session.query(Interest).filter_by(id = data).one()

                user.interests.append(interest_data)

            db.session.add(user)
            db.session.commit()
            return redirect('/')
        else:    
            return render_template("add-interest.html", form=form, choice_combo=choice_combo)
    else:    
        return render_template("add-interest.html", form=form, choice_combo=choice_combo)  