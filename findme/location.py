from os.path import dirname, isfile, join
from json import dump, load
from datetime import datetime, timezone

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
    if _validate(json):
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
    return False

def _validate(json):
    try:
        return abs(json['lat']) <= 90 and abs(json['lng']) <= 180
    except:
        return False