from planit_impact import app
from flask.ext.heroku import Heroku
import os

heroku = Heroku(app)

app.config.update(
	# For local development, uncomment and put in your own user name
    DEBUG = True,
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI'),
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID'),
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY'),
    S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
)
