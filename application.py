from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dunno'

class NameForm(FlaskForm):
    name = StringField("Username", validators = [DataRequired()])
    password = StringField("Password", validators = [DataRequired()])
    login = SubmitField("Login")

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route("/")
def main():
    return render_template('layout.html')


@app.route("/hello")
def testing():
    names = ['AA', 'BB', 'CC']
    print(names)
    testing = "AAA"

    return render_template('template.html', names_arr=names)
    # return "hello"

@app.route("/login", methods = ['GET','POST'])
def login():
    name = None
    password = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
    return render_template('login.html', form=form,name=name,password=password)

if __name__ == "__main__":
    app.run()

