import requests
import json
import pandas as pd
import os

# call API key for basic auth
key_id = os.getenv('CHIDATAPORTAL_ID')
key_secret = os.getenv('CHIDATAPORTAL_SECRET')

# Load API call details
with open('config.json') as js:
    cfg = json.load(js)

url = cfg['base'] + '?' + cfg['where'] + '&' + cfg['limit']

response = requests.get(url, auth=(key_id, key_secret))

df = pd.json_normalize(response.json())
