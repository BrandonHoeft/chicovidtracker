import pandas as pd
from chicovidtracker.api_helpers import load_config, get_env_vars, build_url_from_config
from chicovidtracker.get_api_data import get_api_json

config = load_config("chicovidtracker/api_config.json")
key_id, key_secret = get_env_vars(config['env_vars'])
url = build_url_from_config(config["baseurl"], config["qrystr"])

# get api data, put into dataframe
df = pd.json_normalize(get_api_json(url, key_id, key_secret))