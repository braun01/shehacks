from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome"


@app.route("/hello")
def testing():
    return render_template('template.html')
    # return "hello"

if __name__ == "__main__":
    app.run()

