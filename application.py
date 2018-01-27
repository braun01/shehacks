from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome"


@app.route("/testing")
def testing():
    return render_template("template.html")

if __name__ == "__main__":
    app.run()

