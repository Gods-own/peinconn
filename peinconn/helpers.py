from flask import redirect, request, session
from functools import wraps
from .extensions import db

def login_required(f):
    """
    Decorate routes to require login.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def acc_for_uniqueness(modelField, filterCond, **kwargs):
    the_model_field = modelField.query.filter_by(**filterCond).first()
    if the_model_field is None:
        print(True)
        dbField = modelField(**kwargs)    
        print(kwargs)
        return dbField 
    else:
        print(False)
        dbField = db.session.query( modelField).filter_by(**filterCond).one()
        return dbField

def redirect_url(default='index'):
    return request.args.get('next') or request.referrer or url_for(default)        

    