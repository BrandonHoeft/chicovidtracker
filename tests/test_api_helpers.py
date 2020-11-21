import pytest
from chicovidtracker.api_helpers import get_env_vars, build_url_from_config

@pytest.fixture
def url_inputs():
    base = "https://data.cityofchicago.org/resource/yhhz-zm2v.json?"
    qry = {'$where': "week_start >= '2020-11-15T00:00:00.000'", '$limit': '1'}
    return base, qry


#def test_load_config_1():


#def test_get_env_vars_1():


def test_build_url_from_config_1(url_inputs):
    expected = 'https://data.cityofchicago.org/resource/yhhz-zm2v.json?%24where=week_start+%3E%3D+%272020-11-15T00%3A00%3A00.000%27&%24limit=1'
    actual = build_url_from_config(*url_inputs)
    message = "expected value: {0}\nactual value: {1}".format(expected, actual)
    assert actual == expected, message
