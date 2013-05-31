import json
from flask import Flask, flash, request, render_template, url_for, redirect, make_response
from werkzeug import secure_filename
import os
from flask.ext.heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)
app.config['DEBUG'] = True

app.config.setdefault('AWS_ACCESS_KEY_ID', os.environ.get('AWS_ACCESS_KEY_ID'))
app.config.setdefault('AWS_SECRET_ACCESS_KEY', os.environ.get('AWS_SECRET_ACCESS_KEY'))
app.config.setdefault('S3_BUCKET_NAME', os.environ.get('S3_BUCKET_NAME'))

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

@app.route('/uploaded')
def uploaded():

	theParameters = {
		'key': request.args['key'],
		'bucket': request.args['bucket'],
		}

	print theParameters
	return render_template('newproject.html', **theParameters)


@app.route('/newproject.html')
def newproject():
	import upload

	AWS_ACCESS_KEY_ID = app.config['AWS_ACCESS_KEY_ID']
	AWS_SECRET_ACCESS_KEY = app.config['AWS_SECRET_ACCESS_KEY']
	theBucket = app.config['S3_BUCKET_NAME']
	
	theParameters = upload.upload_to_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,theBucket)
	return render_template('newproject.html', **theParameters)


@app.route("/report.html")
def report():
    return render_template('report.html')

if __name__ == "__main__":
    app.run()