# from flask import Flask, redirect, render_template, request, session, url_for, Blueprint
# from werkzeug.security import check_password_hash, generate_password_hash
# from ....forms.register import RegistrationForm
# from ....forms.login import LoginForm
# from ....forms.interest import InterestForm
# from country_list import countries_for_language
# from ....models import User, Country, Interest
# from ....helpers import acc_for_uniqueness, login_required, user_already_loggedin, interest_needed
# from ....extensions import db

# activity = Blueprint('activity', __name__)

# @activity.route('/', methods=['GET', 'POST'])
# @login_required
# def index():
#     # countries = dict(countries_for_language('en'))

#     # print([(key, countries[key]) for key in countries.keys()])
#     form = RegistrationForm(request.form)
#     return render_template("index.html", form=form)