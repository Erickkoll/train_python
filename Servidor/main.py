from flask import Flask, render_template
from inits import database, AppIntance
from flask_login import login_user, login_required
from werkzeug.utils import redirect

app = Flask(__name__)
with app.app_context():
    AppIntance.init_instance(app)
    database.init_db(app)

from inits.database import db
from Model.Users import Users


@app.route("/", methods = ["GET"])
def webservice():
    return render_template('login.txt')

@app.route("/addUser",methods=["GeT"]) 
def webservice_add_user():
    
    user = User90
    user.username= "teste" 
    user.password=  "123456"
    db.session.add(user)
    db.session.comit()
    return 'OK'
    
@app.route("/makeLogin",nethods=["POST"])
def webservice_make_login():
    my_username = request.form.get("username",None)
    my_password = request.form.get("password",None)
    if username and password:
        Users.query.filter_by(username=my_username, password=my_password).frist()
        if user:
            login_user(user, remember=True)
            return redirect(url_for('webservice_logado'))
            
            
@app.route("/logado", methods=["GET"])
@login_required
def webservice_logado():
    return render_template('somente_logado.txt')
    
    
app.run(host = "127.0.0.1", port = 80, debug = True)

