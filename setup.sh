if [ ! -f .venv/.Python ]; 
	then
	virtualenv .venv --distribute
fi

source .venv/bin/activate
pip install -r requirements.txt

export 'AWS_ACCESS_KEY_ID=AKIAILTHASEMST65HDSQ'
export 'S3_BUCKET_NAME=planit-impact-models'
export 'AWS_SECRET_ACCESS_KEY=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'