from datetime import datetime
from flask import abort, Flask, jsonify, render_template, request
from os import environ
from flask_basicauth import BasicAuth
from numbers import Number

_data = {
    'last_updated': str(datetime.now()),
    'position': {
        'lat': 50,
        'lng': 50
    }
}

app = Flask(__name__)
app.config['BASIC_AUTH_FORCE'] = True
app.config['BASIC_AUTH_USERNAME'] = environ['BASIC_AUTH_USERNAME']
app.config['BASIC_AUTH_PASSWORD'] = environ['BASIC_AUTH_PASSWORD']

BasicAuth(app)

@app.route('/data')
def data():
    return jsonify(_data)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', google_maps_api_key = environ['GOOGLE_MAPS_API_KEY'], last_updated = _data['last_updated'])
    json = request.get_json()
    if _validate(json):
        _data['last_updated'] = str(datetime.now())
        _data['position']['lat'] = json['lat']
        _data['position']['lng'] = json['lng']
        return ''
    else:
        abort(400)

def _validate(json):
    try:
        return abs(json['lat']) <= 90 and abs(json['lng']) <= 180
    except:
        return False