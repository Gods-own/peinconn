from flask import redirect, request, session, url_for, current_app, make_response, jsonify
from functools import wraps
from peinconn.peinconn.extensions import db
from peinconn.peinconn.models import User, Interest
from werkzeug.utils import secure_filename
import os
# from peinconn.peinconn import app

def login_required(f):
    """
    Decorate routes to require login.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        # else:
        #     user_interest = User.query.filter(User.interests.any(id=session['user_id'])).all()
        #     if len(user_interest) < 1:
        #         return redirect('/add-interests')     
        return f(*args, **kwargs)
    return decorated_function

def user_already_loggedin(f):
    """
    Decorate routes to require login.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is not None:
            user_interest = User.query.filter(User.interests.any(id=session['user_id'])).all()
            if len(user_interest) < 1:
                return redirect('/add-interests') 
            else:
                return redirect('/')    
        return f(*args, **kwargs)
    return decorated_function

def interest_needed(f):
    """
    Decorate routes to require login.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_interest = User.query.filter(User.interests.any(id=session['user_id'])).all()
        if len(user_interest) > 1:
            return redirect('/') 
        return f(*args, **kwargs)
    return decorated_function    

# def interest_needed():
#     user_interest = User.query.filter(User.interests.any(id=session['user_id'])).all()
#     print(user_interest)
#     print('good')
#     if len(user_interest) < 1:
#         return redirect('/add-interests')
#     else:
#         return redirect('/')    

def uniqueColumn(tb_name, tb_column, column_data):
    message = f'{tb_column} already exists'

    is_data_exists = db.session.query(db.exists().where(tb_name == column_data)).scalar()

    if is_data_exists == True:
        return make_response(jsonify({'success': False, 'code': 400, 'message': message}), 400) 
    else:
        return True

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

def save_file(file, filename):    

    ALLOWED_EXTENSIONS = ['webm', 'png', 'jpg', 'jpeg']

    is_allowed_extension = '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    if is_allowed_extension:

        new_filename = secure_filename(file.filename)

        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        return new_filename

def remove_file(filename):    

    path = os.getcwd()

    print(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
   
def get_file_url(filename, transformer, transformer_field):
    url_tupple = (current_app.config['APP_URL'], 'static', filename )

    transformer[transformer_field] = "/".join(url_tupple)

    return transformer

    