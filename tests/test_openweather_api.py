import pytest
from os import getenv
from openweather_api import get_weather_url, get_weather
from unittest.mock import patch


@pytest.fixture(scope='session')
def weather_api_key():
    return getenv("WEATHER_API_KEY")


def test__get_weather__output_keys_match_expected():
    city = 'Moscow'
    expected_output_keys = ['temperature', 'feels_like', 'description']
    mock_response = {'temperature': 3.17, 'feels_like': 0.33, 'description': 'overcast clouds'}
    with patch('main.get_weather', return_value=mock_response):
        expected_output = get_weather(city)
        assert set(expected_output_keys) == set(expected_output)


@pytest.mark.parametrize(
    "city, expected_output",
    [
        ("Dogville", {'message': 'city not found'}),
        ("Tbili", {'message': 'city not found'}),
    ]
)
def test__get_weather__returns_message_for_incorrect_city(city, expected_output):
    assert get_weather(city) == expected_output

@pytest.mark.parametrize(
    "city, expected_output",
    [
        ("Yerevan", dict),
        ("Gyumri", dict),
    ]
)
def test__get_weather__returns_correct_types_for_valid_city_names(city, expected_output):
    assert isinstance(get_weather(city), expected_output)


@pytest.mark.parametrize(
    "city, weather_api_key",
    [
        ("Moscow", weather_api_key),
        ("Almaty", weather_api_key),
    ]
)
def test__get_weather_url__returns_correct_types(city, weather_api_key):
    url, params = get_weather_url(city, weather_api_key)
    assert isinstance(url, str)
    assert isinstance(params, dict)


def test__get_weather_url__returns_correct_url(weather_api_key):
    city = 'Atyrau'
    expected_url = 'https://api.openweathermap.org/data/2.5/weather'
    expected_params = {
        'q': city,
        'appid': weather_api_key,
        'units': 'metric',
        'lang': 'en'
    }
    url, params = get_weather_url(city, weather_api_key)
    assert (url, params) == (expected_url, expected_params)
