from urllib.parse import urlencode  # serialize URL encodings from dict
import json
import os

def load_config():
    """Load the api_config.json file."""
    with open("chicovidtracker/api_config.json") as js:
        config = json.load(js)
    return config


def get_env_vars(var_list):
    """get preconfigured OS environment variable values

    Parameters
    ----------
    var_list : list
        list of environment variables. case insensitive

    Returns
    -------
    str
        a str or a list of strings depending on parameter input length
    """
    var_list_upper = [*map(str.upper, var_list)]
    environ_vars = [os.getenv(name) for name in var_list_upper]
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