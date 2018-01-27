from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dunno'


class LoginForm(FlaskForm):
    name = StringField("Username", validators = [DataRequired()])
    password = StringField("Password", validators = [DataRequired()])
    login = SubmitField("Login")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    name = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    register = SubmitField("Register")


manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


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
    name = None
    password = None
    register = RegisterForm()
    if register.validate_on_submit():
        name = register.name.data
        password = register.password.data
    return render_template('register.html', form=register, email = email, name=name, password=password)


if __name__ == "__main__":
    app.run()

