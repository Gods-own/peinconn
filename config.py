from dotenv import load_dotenv
import os
from tempfile import mkdtemp

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    FLASK_APP = os.getenv("FLASK_APP")

    ENV = os.getenv("FLASK_ENV")

    FLASK_RUN_PORT = os.getenv("FLASK_RUN_PORT")

    DEBUG = os.getenv("FLASK_DEBUG")

    SECRET_KEY=os.getenv("SECRET_KEY")

    SESSION_FILE_DIR = mkdtemp()

    SESSION_PERMANENT = False

    SESSION_TYPE = "filesystem"

    TEMPLATES_AUTO_RELOAD = True

    UPLOAD_FOLDER = 'peinconn/static/images/users/uploads'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(basedir, 'peinconn.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = True  

    SESSION_COOKIE_SECURE = False