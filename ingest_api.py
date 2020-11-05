import requests
import configparser
import pandas as pd

parser = configparser.ConfigParser()
parser.read('config.ini')

response = requests.get(parser['api']['url'])

df = pd.json_normalize(response.json())