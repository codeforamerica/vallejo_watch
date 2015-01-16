import os
import urllib
import requests

GOOGLE_API_KEY_FNAME = './.google_api_key'

class Point():
    def __init__(self, x, y):
        self.lon = x
        self.lat = y


def load_google_api_key():
    if os.path.isfile(GOOGLE_API_KEY_FNAME):
        with open(GOOGLE_API_KEY_FNAME) as f:
            api_key = f.read().strip()

        return api_key


def geocode(address):
    api_key = load_google_api_key()
    lat, lon = None, None

    if api_key:

        data = {'address': address + ' Vallejo, CA', 'key': api_key}  # for now assume all addresses are within vallejo
        url = 'https://maps.googleapis.com/maps/api/geocode/json?%s' % urllib.urlencode(data)

        r = requests.get(url) 
        if r.status_code == 200:
            response = r.json()
            status = response.get('status')
            if status == 'OK':
                results = response.get('results')
                if results:
                    point = results[0]['geometry']['location']
                    lat = point['lat']
                    lon = point['lng']

    return Point(lon, lat)
