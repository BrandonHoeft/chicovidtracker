import pytest
import json
from chicovidtracker.api_helpers import load_config, get_env_vars, build_url_from_config

# fixture setup
# setup - bringing the test's env to a state where testing can begin
# teardown/cleanup - bring the environment to clean, original state when test ends
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


@pytest.fixture  # https://docs.pytest.org/en/stable/monkeypatch.html#monkeypatching-environment-variables
def mock_two_env_vars(monkeypatch):
    monkeypatch.setenv("SHELL", "/bin/bash")
    monkeypatch.setenv("USER", "Hedwig")


@pytest.fixture
def mock_missing_env_var(monkeypatch):
    monkeypatch.delenv("HOME", raising=False)


def test_load_config_1(config_filepath):
    """test the return value is a dict"""
    assert isinstance(load_config(config_filepath), dict)


def test_load_config_2(config_filepath):
    """test the data inside the config_filepath fixture is as expected"""
    actual = load_config(config_filepath)
    assert len(actual) == 2
    assert actual['name'] == "Severus Snape"
    assert actual['positions'][0] == "Potions Master"


def test_get_env_vars_1(mock_two_env_vars):
    """test pulling environment variables from OS"""
    inputs = ['SHELL', 'USER']
    assert get_env_vars(inputs) == ['/bin/bash', 'Hedwig']


# https://docs.pytest.org/en/stable/assert.html#assertions-about-expected-exceptions
def test_key_error_get_env_vars_2(mock_missing_env_var):
    """If get_env_vars() raises KeyError with specific message under this mocked
    environment variable test, the test passes"""
    expected_exception_msg = "'HOME' is not an environment variable"
    with pytest.raises(KeyError) as exception_info:
        get_env_vars(['HOME', 'HISTSIZE'])
    assert exception_info.match(expected_exception_msg)


def test_build_url_from_config_1(url_inputs):
    expected = 'https://data.cityofchicago.org/resource/yhhz-zm2v.json?%24where=week_start+%3E%3D+%272020-11-15T00%3A00%3A00.000%27&%24limit=1'
    actual = build_url_from_config(*url_inputs)
    message = "expected value: {0}\nactual value: {1}".format(expected, actual)
    assert actual == expected, message
