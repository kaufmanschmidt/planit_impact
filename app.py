import json
from flask import Flask, flash, request, render_template, url_for, redirect, make_response
from werkzeug import secure_filename
import os, base64, hmac, hashlib, datetime, uuid
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

	if request.headers.get('Accept') == 'application/json':
		theResponse = make_response(json.dumps(theParameters), 200)
		theResponse.headers['Content-Type'] = 'application/json'
		return theResponse
	else:
		return render_template('uploaded.html', **theParameters)


@app.route('/newproject.html')
def newproject():
	if request.args.get('uploaded', False):
		flash('Uploaded! %s' % request.args['key'])

	theNow = datetime.datetime.utcnow()
	# TODO: remove sub-seconds
	theTTL = datetime.timedelta(minutes = 5)
	theExpiration = theNow + theTTL
	# TODO: hack alert!
	theNow = theNow.isoformat() + 'Z'
	theExpiration = theExpiration.isoformat() + 'Z'

	AWS_ACCESS_KEY_ID = app.config['AWS_ACCESS_KEY_ID']
	AWS_SECRET_ACCESS_KEY = app.config['AWS_SECRET_ACCESS_KEY']
	theBucket = app.config['S3_BUCKET_NAME']

	thePath = '/%s' % uuid.uuid4().hex
	theRedirect = url_for('uploaded', _external = True)
	theACL = 'private'
	thePolicy = {
		'expiration': theExpiration,
		'conditions': [ 
			{'bucket': theBucket}, 
			['starts-with', '$key', '%s/' % thePath],
			{'acl': theACL},
			{'success_action_redirect': theRedirect},
			['starts-with', '$Content-Type', ''],
			['content-length-range', 0, 1048576]
		  ]
		}
	thePolicy = json.dumps(thePolicy)
	thePolicy = base64.b64encode(thePolicy)

	theSignature = base64.b64encode(hmac.new(AWS_SECRET_ACCESS_KEY, thePolicy, hashlib.sha1).digest())

	theParameters = {
		'bucket': theBucket,
		'policy': thePolicy,
		'signature': theSignature,
		'redirect':  theRedirect,
		'acl':  theACL,
		'AWS_ACCESS_KEY_ID': AWS_ACCESS_KEY_ID,
		'key': '%s/${filename}' % thePath,
		'url': 'https://%s.s3.amazonaws.com/' % theBucket,
		'encoding': 'multipart/form-data',
		'expiration': theExpiration,
		'now': theNow,
		'ttl': theTTL.total_seconds(),
		}

	if request.headers.get('Accept') == 'application/json':
		theResponse = make_response(json.dumps(theParameters), 200)
		theResponse.headers['Content-Type'] = 'application/json'
		return theResponse
	else:
		return render_template('newproject.html', **theParameters)

@app.route("/report.html")
def report():
    return render_template('report.html')

if __name__ == "__main__":
    app.run()