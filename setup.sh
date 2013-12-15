if [ ! -f .venv/.Python ]; 
	then
	virtualenv .venv --distribute
fi

source .venv/bin/activate
pip install -r requirements.txt

# Add your AWS credentials here to run locally.
export 'SQLALCHEMY_DATABASE_URI=postgres://hackyourcity@localhost/planit'
export 'AWS_ACCESS_KEY_ID=XXXXXXXXX'
export 'S3_BUCKET_NAME=planit-impact-models'
export 'AWS_SECRET_ACCESS_KEY=XXXXXXXXXXX'