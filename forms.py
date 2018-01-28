from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    login = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    firstname = StringField("First Name", validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    cpassword = PasswordField("Confirm Password", validators=[DataRequired()])
    register = SubmitField("Register")

class CreateProjectForm(FlaskForm):
    projectName = StringField("Project Name", validators=[DataRequired()])
    color = StringField("Color", validators=[DataRequired()])
    dueDate = StringField("Due Date", validators=[DataRequired()])
    estimatedTime = StringField("Estimated Length", validators=[DataRequired()])
    workDays = StringField("What days do you want to work?", validators=[DataRequired()])
    priority = StringField("Priority from 1-10: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

