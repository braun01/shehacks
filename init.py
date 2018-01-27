from flask import Flask
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\Annie\\UIUC\\Freshman\\Semester 2\\Other\\shehacks\\db\\database.db'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


