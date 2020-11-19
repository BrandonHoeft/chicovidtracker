import requests
import pandas as pd
from api_helpers import build_url_from_config, get_env_vars

# call API key for basic auth
key_id = get_env_vars('CHIDATAPORTAL_ID')
key_secret = get_env_vars('CHIDATAPORTAL_SECRET')
url = build_url_from_config("baseurl", "qrystr")

def get_api_json(target_url, api_key, api_secret):
    """make get request to Socrata Chicago Data Portal API

    Parameters
    ----------
    target_url : str
        a validly formed URL string
    api_key : str
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
    api_response = requests.get(target_url, auth=(api_key, api_secret))

    try:
        api_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # return errors from bad requests
        return f"error: {e}"

    # if a successful response status code
    return api_response.json()


# get api data, put into dataframe
df = pd.json_normalize(get_api_json(url, key_id, key_secret))
