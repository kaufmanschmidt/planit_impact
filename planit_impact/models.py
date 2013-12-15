from flask.ext.sqlalchemy import SQLAlchemy
from planit_impact import app

db = SQLAlchemy(app)

#----------------------------------------
# models
#----------------------------------------

class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    description = db.Column(db.Unicode)
    s3_url = db.Column(db.Unicode)
    s3_name = db.Column(db.Unicode)
    settings_json = db.Column(db.Unicode)

    def upload_to_s3(self, name, localpath):
        conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
        mybucket = conn.get_bucket(S3_BUCKET_NAME)
        k = Key(mybucket)
        k.key = name
        k.set_contents_from_filename(localpath)
        mybucket.set_acl('public-read', name)
        conn.close()
        self.s3_name = name
        self.s3_url = 'https://s3.amazonaws.com/%s/'% S3_BUCKET_NAME + name

    def download_from_s3(self):
        conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
        mybucket = conn.get_bucket(S3_BUCKET_NAME)
        k = Key(mybucket)
        k.key = self.s3_name
        content = k.get_contents_as_string()
        conn.close()
        return content

    @property
    def kmz_url(self):
        return self.s3_url
