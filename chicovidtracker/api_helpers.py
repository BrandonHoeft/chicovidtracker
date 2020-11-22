from urllib.parse import urlencode  # serialize URL encodings from dict
import json
import os


def load_config(path_str):
    """Load the api_config.json file."""
    with open(path_str) as js:
        config = json.load(js)
    return config


def get_env_vars(var_list):
    """get preconfigured OS environment variable values

    Parameters
    ----------
    var_list : list
        list of environment variables. case insensitive

    Raises
    -------
    KeyError
        raised when an environment variable does not exist in the OS

    Returns
    -------
    str
        a str or a list of strings depending on parameter input length
    """
    var_list_upper = [*map(str.upper, var_list)]
    environ_var_values = []
    for i, var in enumerate(var_list_upper):
        try:
            environ_var_values.append(os.environ[var])
        except KeyError as e:
            print(f"Error: value at position {i}, {e}, is not an environment variable")
    return environ_var_values


def build_url_from_config(base_str, query_str):
    """build encoded URL string for Socrata Chicago Data Portal API

    Parameters
    ----------
    base_str : the "baseurl" key in api_config.json
    query_str : the "qrystr" key in api_config.json

    Returns
    -------
    str
        a valid URL string for the API

    """
    return base_str + urlencode(query_str)

