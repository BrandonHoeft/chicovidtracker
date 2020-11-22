import requests
import pandas as pd
from chicovidtracker.api_helpers import load_config, get_env_vars, build_url_from_config

config = load_config("chicovidtracker/api_config.json")
key_id, key_secret = get_env_vars(config['env_vars'])
url = build_url_from_config(config["baseurl"], config["qrystr"])

def get_api_json(target_url, api_id, api_secret):
    """make get request to Socrata Chicago Data Portal API

    Parameters
    ----------
    target_url : str
        a validly formed URL string
    api_id : str
        API key id for HTTP basic auth
    api_secret : str
        API secret passcode for HTTP basic auth

    Raises
    ------
    RequestException
        base exception class for requests library

    Returns
    -------
    list
        if successful, a list of dicts is returned
    """
    try:
        api_response = requests.get(target_url, auth=(api_id, api_secret))
        api_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"error: {e}"

    # if a successful response status code
    return api_response.json()


# get api data, put into dataframe
df = pd.json_normalize(get_api_json(url, key_id, key_secret))