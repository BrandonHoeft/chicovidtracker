import pytest
import json
from chicovidtracker.api_helpers import load_config, get_env_vars, build_url_from_config

# fixtures get passed as args to tests to facilitate:
# setup - bringing env to a state where testing can begin
# teardown/cleanup - bring environment to clean, original state after test ends
@pytest.fixture
def url_inputs():
    base = "https://data.cityofchicago.org/resource/yhhz-zm2v.json?"
    qry = {'$where': "week_start >= '2020-11-15T00:00:00.000'", '$limit': '1'}
    return base, qry


@pytest.fixture
def config_filepath(tmpdir):  # tmpdir is a chained pytest fixture
    """create temporary config dir and data for testing load_config()"""
    test_config_path = tmpdir.join("test_config.json")
    data = {"name": "Severus Snape",
            "positions": ["Potions Master", "Defense Against the Dark Arts"]}
    with open(test_config_path, "w") as f:
        json.dump(data, f)
    yield test_config_path


def test_load_config_1(config_filepath):
    """test the return value is a dict"""
    assert isinstance(load_config(config_filepath), dict)


def test_load_config_2(config_filepath):
    """test the data inside the config_filepath fixture is as expected"""
    actual = load_config(config_filepath)
    assert len(actual) == 2
    assert actual['name'] == "Severus Snape"
    assert actual['positions'][0] == "Potions Master"


#def test_get_env_vars_1():


def test_build_url_from_config_1(url_inputs):
    expected = 'https://data.cityofchicago.org/resource/yhhz-zm2v.json?%24where=week_start+%3E%3D+%272020-11-15T00%3A00%3A00.000%27&%24limit=1'
    actual = build_url_from_config(*url_inputs)
    message = "expected value: {0}\nactual value: {1}".format(expected, actual)
    assert actual == expected, message
