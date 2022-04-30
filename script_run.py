# was testing out the API here 
import requests

import json

resp = requests.get('https://api.openweathermap.org/data/2.5/weather?')
data_files = resp.json

humidity = data_files['main']['humidity']
pressure = data_files['main']['pressure']
wind = data_files['wind']['speed']
description = data_files['weather'][0]['description']
temp = data_files['main']['temp']