import requests
from os import getenv
from typing import Optional, Any


def get_weather_url(city: str, weather_api_key: Optional[str]) -> tuple[str, dict[str,  Optional[str]]]:
    params = {
        "q": city,
        "appid": weather_api_key,
        "units": "metric",
        "lang": "en",
    }
    return "https://api.openweathermap.org/data/2.5/weather", params


def get_weather_data(url: str, params: dict[str, Optional[str]]) -> dict:
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_weather(city: str) -> dict[str, float]:
    weather_api_key: Optional[str] = getenv("WEATHER_API_KEY")
    url, params = get_weather_url(city, weather_api_key)
    try:
        data = get_weather_data(url, params=params)
    except requests.exceptions.HTTPError as error:
        error_message = error.response.json().get('message', 'City not found')
        return {'message': error_message}
    return parse_weather_data(data)


def parse_weather_data(data: dict[str, Any]) -> dict[str, Any]:
    return {
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "description": data["weather"][0]["description"],
    }
