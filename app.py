import json
from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/features.html")
def features():
    return render_template('features.html')

@app.route("/howitworks.html")
def howitworks():
    return render_template('howitworks.html')

@app.route("/newproject.html")
def newproject():
    return render_template('newproject.html')

@app.route("/report.html")
def report():
    return render_template('report.html')

if __name__ == "__main__":
    app.run()