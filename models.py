from init import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class User(db.Model):
    email = db.Column(db.String(80), primary_key=True, unique=True)
    password = db.Column(db.String(80))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.email)


class Project(db.Model):
    projectName = db.Column(db.String(80), primary_key= True, unique=True)
    color = db.Column(db.String(80))
    dueDate = db.Column(db.String(80))
    estimatedTime = db.Column(db.String(80))
    workDays = db.Column(db.String(80))
    priority = db.Column(db.Integer)
    username = db.Column(db.String(80))

    def __init__(self, projectName):
        self.projectName = projectName

    def __repr__(self):
        return '<User %r>' % self.projectName

    def completed(self):
        return True
