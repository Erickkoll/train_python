from inits.database import db #inits ***
from sqlalchemy import types
from flask_login import UserMixin
from inits.AppIntance import login_manager

class Users(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(types.TEXT, unique = True, nullable = False)
    password = db.Column(types.TEXT, nullable = False)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))
        
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.id