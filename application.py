from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from forms import RegisterForm, LoginForm
from models import db
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database/database.sqlite'


manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/hello")
def testing():
    names = ['AA', 'BB', 'CC', 'DD', 'EE']
    print(names)
    testing = "AAA"

    return render_template('template.html', names_arr=names)
    # return "hello"


@app.route("/login", methods=['GET', 'POST'])
def login():
    name = None
    password = None
    login = LoginForm()
    if login.validate_on_submit():
        name = login.name.data
        password = login.password.data
    return render_template('login.html', form=login, name=name, password=password)


@app.route("/register", methods=['GET', 'POST'])
def register():
    email = None
    firstname = None
    lastname = None
    username = None
    password = None
    register = RegisterForm()
    if register.validate_on_submit() and register.password.data == register.cpassword.data:
        username = register.username.data
        password = register.password.data
    else:
        return render_template('register.html', form=register)
    return render_template('register.html', form=register, email=email, firstname=firstname, lastname=lastname,
                           username=username, password=password)


if __name__ == "__main__":
    app.run()

