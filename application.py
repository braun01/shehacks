from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run()

