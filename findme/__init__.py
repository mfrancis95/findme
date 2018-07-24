from flask import abort, Flask, render_template, request, send_file
from os import environ
from flask_basicauth import BasicAuth
from findme.location import update_location

app = Flask(__name__)
app.config['BASIC_AUTH_FORCE'] = True
app.config['BASIC_AUTH_USERNAME'] = environ['BASIC_AUTH_USERNAME']
app.config['BASIC_AUTH_PASSWORD'] = environ['BASIC_AUTH_PASSWORD']

BasicAuth(app)

@app.route('/')
def index():
    return render_template('index.html', google_maps_api_key = environ['GOOGLE_MAPS_API_KEY'])

@app.route('/location', methods = ['GET', 'POST'])
def location():
    if request.method == 'GET':
        return send_file('location.json', cache_timeout = 60, conditional = True)
    if update_location(request.get_json()):
        return ''
    abort(400)