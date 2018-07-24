from os.path import dirname, isfile, join
from datetime import datetime, timezone
from json import dump

_file = join(dirname(__file__), 'location.json')

if not isfile(_file):
    with open(_file, 'w') as fp:
        data = {
            'last_updated': datetime.now(timezone.utc).isoformat(),
            'position': {
                'lat': 50,
                'lng': 50
            }
        }
        dump(data, fp)

def update_location(json):
    if not _validate(json):
        return False
    with open(_file, 'w') as fp:
        data = {
            'last_updated': datetime.now(timezone.utc).isoformat(),
            'position': {
                'lat': json['lat'],
                'lng': json['lng']
            }
        }
        dump(data, fp)
    return True

def _validate(json):
    try:
        return abs(json['lat']) <= 90 and abs(json['lng']) <= 180
    except:
        return False