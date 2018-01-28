# Project Project

## To get Flask up and running
First, navigate to the direction containing `application.py`. On a Mac, first run the following: `export FLASK_APP=application.py` and then `export FLASK_DEBUG=1`. 

On a PC, first run `set FLASK_APP=application.py` and then `set FLASK_DEBUG=1`.

From that point, get Flask running using `flask run`. The above steps need to be re-done every time you open a new terminal window.

## Installing packages
Pip is required to install these packages
1. `pip install Flask`
2. `pip install flask_script`
3. `pip install flask_bootstrap`
4. `pip install flask_moment`
5. `pip install flask_wtf`
6. `pip install flask_login`
7. `pip install flask_sqlalchemy`

## Database
Make sure you update the path of `app.config['SQLALCHEMY_DATABASE_URI']` to where your computer stores the database.

## Helpful Links for Flask
<https://pythonspot.com/flask-web-app-with-python/>
