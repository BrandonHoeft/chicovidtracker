from urllib.parse import urlencode  # serialize URL encodings from dict
import json
import os

def get_env_vars(env_var):
    return os.getenv(env_var)


def build_url_from_config(base_str, query_str):
    # Load API call details
    with open('api_config.json') as js:
        cfg = json.load(js)
    return cfg[base_str] + urlencode(cfg[query_str])