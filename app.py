import os, json, boto, requests, zipfile
from flask import Flask, flash, request, render_template, url_for, redirect, make_response, send_from_directory, flash
from werkzeug import secure_filename
from flask.ext.heroku import Heroku
from pykml import parser

app = Flask(__name__)
heroku = Heroku(app)
app.config['DEBUG'] = True

app.config.setdefault('AWS_ACCESS_KEY_ID', os.environ.get('AWS_ACCESS_KEY_ID'))
app.config.setdefault('AWS_SECRET_ACCESS_KEY', os.environ.get('AWS_SECRET_ACCESS_KEY'))
app.config.setdefault('S3_BUCKET_NAME', os.environ.get('S3_BUCKET_NAME'))

@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/about")
@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/features")
@app.route("/features.html")
def features():
    return render_template('features.html')

@app.route("/howitworks")
@app.route("/howitworks.html")
def howitworks():
    return render_template('howitworks.html')

@app.route("/demo", methods=['GET', 'POST'])
@app.route("/demo.html", methods=['GET', 'POST'])
def demo():
	if request.method == 'POST':
		file = request.files['file']
		if '.kmz' in file.filename:
			filename = secure_filename(file.filename)
			filepath = 'static/models/'+filename
			file.save(filepath)
			flash(filename)
			get_model_data(filename)
		else:	 
			flash('Only kmz files allowed.')
		return render_template('demo.html')
		
	model_names = []
	conn = boto.connect_s3()
	mybucket = conn.get_bucket('planit-impact-models') # Substitute in your own bucket name
	file_list = mybucket.list()
	conn.close()
	for file_path in file_list:
		model_names.append(file_path.name)
	return render_template('demo.html', model_names = model_names)


# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)                        

	# import upload_s3

# 	AWS_ACCESS_KEY_ID = app.config['AWS_ACCESS_KEY_ID']
# 	AWS_SECRET_ACCESS_KEY = app.config['AWS_SECRET_ACCESS_KEY']
# 	theBucket = app.config['S3_BUCKET_NAME']
	
# 	theParameters = upload_s3.upload_to_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,theBucket)

# 	# Download existing models
# 	model_names = []
# 	conn = boto.connect_s3()
# 	mybucket = conn.get_bucket('planit-impact-models') # Substitute in your bucket name
# 	file_list = mybucket.list()
# 	for file_path in file_list:
# 		model_names.append(file_path.name)

# 	return render_template('demo', model_names=model_names, **theParameters)

# @app.route('/project/<model_name>')
# def project(model_name):

# 	#Download model
# 	r = requests.get('https://s3.amazonaws.com/planit-impact-models/'+model_name)
# 	with open('static/models/'+model_name, "wb") as new_model:
# 	    new_model.write(r.content)

# 	# Get the lat and lon from the model.
# 	import zipfile
# 	z = zipfile.ZipFile('static/models/'+model_name)
# 	z.extractall('static/models/')
# 	from pykml import parser
# 	with open('static/models/doc.kml') as f:
# 		doc = parser.parse(f)

# 	root = doc.getroot()
# 	lat = root.Placemark.Model.Location.latitude
# 	lon = root.Placemark.Model.Location.longitude
# 	import pdb
# 	pdb.set_trace()

# 	return render_template('project.html', model_name=model_name, lat=lat, lon=lon)


# def get_lat_lon(model_name):



@app.route("/project/<model_name>/report/explore")
def report(model_name):
    return render_template('explore.html', model_name=model_name)

if __name__ == "__main__":
    app.run()