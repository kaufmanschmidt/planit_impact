from flask import request, url_for
import base64, hmac, hashlib, datetime, json

def upload_to_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,theBucket):
	theNow = datetime.datetime.utcnow()
	# TODO: remove sub-seconds
	theTTL = datetime.timedelta(minutes = 5)
	theExpiration = theNow + theTTL
	# TODO: hack alert!
	theNow = theNow.isoformat() + 'Z'
	theExpiration = theExpiration.isoformat() + 'Z'

	thePath = '%s' % 'models' #uuid.uuid4().hex
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

	return theParameters