from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

# Calls an example API to get some data from cartodb
longitude = str(-94.58083)
latitude = str(39.08971)

@app.route('/neighborhood', methods=['POST', 'GET'])
def neighborhood():
	url = 'http://cfa.cartodb.com/api/v2/sql?q='
	url = url + 'SELECT%20nbhname%20FROM%20kc_census_hoods%20WHERE%20'
	url = url + 'ST_CONTAINS(the_geom,%20ST_GeomFromText(\'POINT('+longitude+'%20'+latitude+')\',%204326))'
	r = requests.get(url)
	rjson = r.json
	nbhname = rjson['rows'][0]['nbhname']
	return render_template('neighborhood.html', nbhname = nbhname)

# ToDo: Google Earth template that zooms to this neighborhood

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port, debug="true")
