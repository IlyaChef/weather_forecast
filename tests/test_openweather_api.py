import pytest
from os import getenv
from openweather_api import get_weather_url, get_weather


WEATHER_API_KEY = getenv("WEATHER_API_KEY")


@pytest.mark.parametrize(
    "city, expected_output_keys",
    [
        ("Moscow", ['temperature', 'feels_like', 'description']),
        ("Almaty", ['temperature', 'feels_like', 'description']),
    ]
)
def test__get_weather__output_keys_match_expected(city, expected_output_keys):
    assert set(expected_output_keys) == set(get_weather(city).keys())


@pytest.mark.parametrize(
    "city, expected_output",
    [
        ("Dogville", {'message': 'City not found'}),
        ("Tbili", {'message': 'City not found'}),
    ]
)
def test__get_weather__returns_message_for_incorrect_city(city, expected_output):
    assert get_weather(city) == expected_output


@pytest.mark.parametrize(
    "city, expected_output",
    [
        ("Erevan", dict),
        ("Gyumri", dict),
    ]
)
def test__get_weather__returns_correct_types_for_valid_city_names(city, expected_output):
    assert isinstance(get_weather(city), expected_output)


@pytest.mark.parametrize(
    "city, WEATHER_API_KEY",
    [
        ("Moscow", WEATHER_API_KEY),
        ("Almaty", WEATHER_API_KEY),
    ]
)
def test__get_weather_url__returns_correct_types(city, WEATHER_API_KEY):
    url, params = get_weather_url(city, WEATHER_API_KEY)
    assert isinstance(url, str)
    assert isinstance(params, dict)


def test__get_weather_url__returns_correct_url():
    city = 'Atyrau'
    expected_url = 'https://api.openweathermap.org/data/2.5/weather'
    expected_params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric',
        'lang': 'en'
    }
    url, params = get_weather_url(city, WEATHER_API_KEY)
    assert (url, params) == (expected_url, expected_params)
