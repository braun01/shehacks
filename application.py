from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from forms import RegisterForm, LoginForm, CreateProjectForm
from init import app
from models import db, User, Project
from flask_login import LoginManager, login_user, login_required, logout_user


def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(username = username).first()


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/protected')
@login_required
def protected():
    return "Home Page for Users"

@app.route("/createProject", methods = ['GET','POST'])
def project():
    project = CreateProjectForm()
    if project.validate_on_submit():
        if Project.query.filter_by(projectname=CreateProjectForm.projectName.data).first():
            return render_template('createProject.html', form=project)
        else:
            newproject = Project(CreateProjectForm.projectName.data, CreateProjectForm.color.data,
                                 CreateProjectForm.dueDate.data, CreateProjectForm.estimatedTime.data,
                                 CreateProjectForm.workDays.data, CreateProjectForm.priority.data)
            db.session.add(newproject)
            db.session.commit()
            return render_template('createProject.html', form=project)
    return render_template('createProject.html', form=project)



@app.route("/login", methods=['GET', 'POST'])
def login():
    name = None
    password = None
    login = LoginForm()
    if login.validate_on_submit():
        name = login.name.data
        password = login.password.data
        user = User.query.filter_by(username=LoginForm.name.data).first()
        if user:
            if user.password == LoginForm.password.data:
                login_user(user)
                return "User logged in"
            else:
                return "Wrong password"
        else:
            return "User does not exist"
    else:
        return render_template('login.html', form=login, name=name, password=password)


@app.route("/register", methods=['GET', 'POST'])
def register():
    firstname = None
    lastname = None
    username = None
    password = None
    register = RegisterForm()
    if register.validate_on_submit() and register.password.data == register.cpassword.data:
        if User.query.filter_by(email=RegisterForm.email.data).first():
            return render_template('register.html', form=register)
        else:
            newuser = User(RegisterForm.email.data, RegisterForm.username.data, RegisterForm.password.data)
            db.session.add(newuser)
            db.session.commit()
            username = register.username.data
            password = register.password.data
            email = register.email.data
            login_user(newuser)
            return render_template('createProject.html', form=register, email=email, firstname=firstname, lastname=lastname,
                                   username=username, password=password)
    else:
        return render_template('register.html', form=register)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out"

if __name__ == "__main__":
    init_db()
    app.run()

