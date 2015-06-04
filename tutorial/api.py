
import json
import requests

data = requests.get(url).text
data = json.loads(data)
print type(data)
print data
#data['artist']
#geo.getTopArtists
data['topartists']['artist'][0]['name']
