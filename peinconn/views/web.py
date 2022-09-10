from flask import Flask, redirect, render_template, request, session, url_for, Blueprint
from ..forms.register import RegistrationForm
from country_list import countries_for_language

web = Blueprint('web', __name__)

@web.route('/', methods=['GET', 'POST'])
def index():
    # countries = dict(countries_for_language('en'))

    # print([(key, countries[key]) for key in countries.keys()])
    form = RegistrationForm(request.form)
    return render_template("index.html", form=form)