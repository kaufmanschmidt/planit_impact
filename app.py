import os, json, boto, zipfile, re, pdb
from boto.s3.key import Key
from flask import Flask, flash, request, render_template, url_for, redirect, make_response, send_from_directory, flash
from werkzeug import secure_filename

from flask.ext.heroku import Heroku
from flask.ext.sqlalchemy import SQLAlchemy

try:
    from setup_local import *
except:
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = os.environ.get('S3_BUCKET_NAME')
    SQLALCHEMY_DATABASE_URI = 'postgres://hackyourcity@localhost/planit'

#----------------------------------------
# initialization
#----------------------------------------

app = Flask(__name__)
heroku = Heroku(app)
db = SQLAlchemy(app)

app.config.update(
    DEBUG = True,
    # For local development, uncomment and put in your own user name
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
)

# Might not need these anymore? What config key does boto use?
app.config.setdefault('AWS_ACCESS_KEY_ID', AWS_ACCESS_KEY_ID)
app.config.setdefault('AWS_SECRET_ACCESS_KEY', AWS_SECRET_ACCESS_KEY)
app.config.setdefault('S3_BUCKET_NAME', AWS_SECRET_ACCESS_KEY)

#----------------------------------------
# models
#----------------------------------------

class ThreeDeeModel(db.Model):
    __tablename__ = 'three_dee_model'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    description = db.Column(db.Unicode)
    localpath = db.Column(db.Unicode)
    latitude = db.Column(db.Unicode)
    longitude = db.Column(db.Unicode)
    s3_url = db.Column(db.Unicode)

    def __init__(self, name, description, localpath):
        self.name = name
        self.description = description
        self.localpath = localpath

    def open_model(self):
        z = zipfile.ZipFile(self.localpath)
        z.extractall('tmp')

    def get_lat_lon_from_model(self):
        kml = open('tmp/doc.kml','r').read()
        match = re.search('<latitude>(.*)</latitude>', kml)
        self.latitude = match.group(1)
        match = re.search('<longitude>(.*)</longitude>', kml)
        self.longitude = match.group(1)

    def upload_to_s3(self):
        conn = boto.connect_s3()
        mybucket = conn.get_bucket('planit-impact-models')
        k = Key(mybucket)
        k.key = self.name
        k.set_contents_from_filename(self.localpath)
        conn.close()
        self.s3_url = 'https://s3.amazonaws.com/planit-impact-models/'+self.name

#----------------------------------------
# controllers
#----------------------------------------

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
            try:
                os.mkdir('tmp')
            except:
                pass
            filepath = 'tmp/'+filename
            file.save(filepath)
            description = request.form['description']

            model = ThreeDeeModel(filename,description,filepath)
            model.open_model()
            model.get_lat_lon_from_model()
            model.upload_to_s3()

            db.session.add(model)
            db.session.commit()
        else:
            flash('Only kmz files allowed.') # Still needs a template to make use of this.

    all_models = ThreeDeeModel.query.all()

    return render_template('demo.html', all_models=all_models)

@app.route("/<model_name>/report/explore")
def report(model_name):
    model = ThreeDeeModel.query.filter_by(name=model_name).first()
    return render_template('explore.html', model=model)

if __name__ == "__main__":
    app.run()