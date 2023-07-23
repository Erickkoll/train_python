from flask_login import LoginManager

app Instance = None
login_maneger = None

def init_instance(app):
    global app Instance
    global login_manger
    appInstance = app
    login_manager = LoginManager()
    login_manager.init_app(appInstance)