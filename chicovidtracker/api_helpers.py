from urllib.parse import urlencode  # serialize URL encodings from dict
import json
import os

def load_config():
    """Load the api_config.json file."""
    with open("chicovidtracker/api_config.json") as js:
        config = json.load(js)
    return config


def get_env_vars(*args):
    """get OS environment variable values given the name(s) of env variables

    Parameters
    ----------
    *args : str
        one string, or multiple csv strings. case insensitive

    Returns
    -------
    str
        a str or a list of strings depending on parameter input length
    """
    args_upper = [*map(str.upper, args)]
    environ_vars = []
    for elem in args_upper:
         environ_vars.append(os.getenv(elem))
    return environ_vars


def build_url_from_config(base_str, query_str):
    """ reads api_config.json to build URL for Socrata Chicago Data Portal API

    Parameters
    ----------
    base_str : the "baseurl" key in api_config.json
    query_str : the "qrystr" key in api_config.json

    Returns
    -------
    str
        a hopefully valid URL string for the API

    """
    with open('chicovidtracker/api_config.json') as js:
        cfg = json.load(js)
    return cfg[base_str] + urlencode(cfg[query_str])