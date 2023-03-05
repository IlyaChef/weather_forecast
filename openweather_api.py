import requests
from dotenv import load_dotenv
from os import getenv
from weather_parser import parse_weather_data


load_dotenv()


def get_weather_url(city: str, WEATHER_API_KEY: str) -> tuple[str, dict[str, str]]:
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "en",
    }
    return "https://api.openweathermap.org/data/2.5/weather", params


def get_weather_data(url: str, params: dict[str, str]) -> dict:
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_weather(city: str) -> dict:
    WEATHER_API_KEY = getenv("WEATHER_API_KEY")
    url, params = get_weather_url(city, WEATHER_API_KEY)
    try:
        data = get_weather_data(url, params=params)
    except requests.exceptions.HTTPError as error:
        error_message = error.response.json().get('message', 'City not found')
        return {'message': error_message}
    return parse_weather_data(data)
