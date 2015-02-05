import json
import random
import urllib

from flask import Flask, render_template, request
app = Flask(__name__)

# client id from developer.uber.com/apps
CLIENT_ID = ''

WECODE_LATITUDE = 42.3799673
WECODE_LONGITUDE = 71.1156968

MUBER_URL = 'http://m.uber.com/sign-up?'
LOCATIONS_FILE = 'locations.json'


@app.route('/')
def index():
    """Render the start page."""
    print 'Rendering index.html'
    return render_template('index.html')

@app.route('/explore')
def explore():
    """Render a random location and Uber button."""

    # Load json holding list of locations
    with open(LOCATIONS_FILE, 'r') as f:
        locations = json.load(f)

    # Pick a random location
    location = random.choice(locations['locations_list'])

    # Parse variables for page
    destination = location['label']
    dropoff_latitude = location['lat']
    dropoff_longitude = location['lng']

    time_estimate = 0 # minutes
    price_estimate = ''

    product_id = 'uuid'

    #  Construct deeplinkurl to request a ride
    request_params = {
        'client_id': CLIENT_ID,
        'product_id': product_id,
        'pickup_latitude': WECODE_LATITUDE,
        'pickup_longitude': WECODE_LONGITUDE,
        'dropoff_latitude': dropoff_latitude,
        'dropoff_longitude': dropoff_longitude,
    }
    request_url = MUBER_URL + urllib.urlencode(request_params)

    # Render the page
    return render_template(
        'explore.html',
        destination=destination,
        time_estimate=time_estimate,
        price_estimate=price_estimate,
        request_url=request_url,
    )

if __name__ == '__main__':
    app.run()
