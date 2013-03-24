from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask.views import View
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('website/index.html')

class RenderTemplateView(View):
    def __init__(self, template_name):
        self.template_name = template_name
    def dispatch_request(self):
        return render_template(self.template_name)

#Calls an example API to get some data from cartodb
@app.route('/neighborhood', methods=['POST', 'GET'])
def neighborhood():
    latitude = request.args.get('latitude','')
    longitude = request.args.get('longitude','')

    # Get open 311 cases in the neighborhood
    def get_311(latitude, longitude):
        url = 'http://cfa.cartodb.com/api/v2/sql?q=SELECT%20case_summary,%20latitude,%20longitude%20FROM%20crossroads_311'
        r = requests.get(url)
        cases = r.json['rows']
        return cases

    cases = get_311(latitude,longitude)

    # Get the neighborhood name
    def get_nbhname(latitude, longitude):
        url = 'http://cfa.cartodb.com/api/v2/sql?q='
        url = url + 'SELECT%20nbhname%20FROM%20kc_census_hoods%20WHERE%20'
        url = url + 'ST_CONTAINS(the_geom,%20ST_GeomFromText(\'POINT('+longitude+'%20'+latitude+')\',%204326))'
        r = requests.get(url)
        rjson = r.json
        nbhname = rjson['rows'][0]['nbhname']
        return nbhname

    nbhname = get_nbhname(latitude,longitude)

    return render_template('neighborhood.html', cases = cases, nbhname = nbhname, longitude = longitude, latitude = latitude)

# ToDo: Google Earth template that zooms to this neighborhood

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.add_url_rule('/about', view_func=RenderTemplateView.as_view(
            'about_page', template_name='about.html'))
    app.run(host='0.0.0.0', port=port, debug="true")
