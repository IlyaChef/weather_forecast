import requests
from fastapi import HTTPException
from dotenv import load_dotenv
from os import getenv
from weather_parser import parse_weather_data


load_dotenv()

weather_api_key = getenv("WEATHER_API_KEY")


def get_weather_url(city: str, weather_api_key: str) -> tuple[str, dict[str, str]]:
    params = {
        "q": city,
        "appid": weather_api_key,
        "units": "metric",
        "lang": "en"
    }
    return "https://api.openweathermap.org/data/2.5/weather", params


def get_weather_data(url: str, params: dict = None) -> dict:
    response = requests.get(url, params=params)
    if response.status_code != 200:
        error_message = response.json().get('message', 'City not found')
        raise HTTPException(status_code=response.status_code, detail=error_message)
    return response.json()


def get_weather(city: str, weather_api_key: str) -> dict:
    url, params = get_weather_url(city, weather_api_key)
    data = get_weather_data(url, params=params)
    return parse_weather_data(data)
