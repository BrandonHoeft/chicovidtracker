import requests


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
