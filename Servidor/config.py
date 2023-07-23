import os
basedir = os.path.abspath(os.path.dirname(__name__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')\
                              or 'sqlite:///' + os.path.join(basedir, "flask.db")

    SECRET_KEY = os.urandom(12)
    USERNAME = 'batata'
    PASSWORD = 'python'
    
