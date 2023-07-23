from flask_sqlalchemy import SQLAlchemy

from config import Config

db = None

def init_db(app):
    global db
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    #criar tabelas
    from Model import Users
    db.create_all()
    
