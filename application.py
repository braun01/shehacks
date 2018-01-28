from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, jsonify
from forms import RegisterForm, LoginForm
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database/database.sqlite'


manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route("/")
def main():
    return render_template('index.html')

# This should query the database and determine which projects are still current
# based on current date vs due date
@app.route("/projects")
def projects():

    projects = [{"name": "Essay", \
                "color": "red", \
                "due_date": "01-30-2018 11:59pm", \
                "est_total_time": 6, \
                "work_days": ["Monday", "Wednesday", "Friday"], \
                "priority": "medium", \
                "completed": False}, \
                {"name": "pset", \
                "color": "blue", \
                "due_date": "01-28-2018 11:59pm", \
                "est_total_time": 8, \
                "work_days": ["Thursday", "Friday"], \
                "priority": "high",\
                "completed": False }, \
                {"name": "reading", \
                "color": "orange", \
                "due_date": "02-03-2018 11:59pm", \
                "est_total_time": 1, \
                "work_days": ["Saturday"], \
                "priority": "medium", \
                "completed": False} ] 

    print(projects)
    return jsonify(projects)
    return render_template('projects.html')


# Create Project should just add the new project to the database
# Get project info from the creatProject submit form
@app.route("/createProject")
def testing():
    names = ['AA', 'BB', 'CC', 'DD', 'EE']
    # print(names)
    testing = "AAA"

    # return render_template('createProject.html', names_arr=names)
    return render_template('createProject.html')
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

