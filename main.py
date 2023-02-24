import requests
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from os import getenv


load_dotenv()

app = FastAPI()

weather_api_key = getenv("WEATHER_API_KEY")


def parse_weather_data(data: dict) -> dict:
    return {
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "description": data["weather"][0]["description"],
    }


def get_weather_url(city: str, weather_api_key: str) -> str:
    return f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric&lang=en"


def get_weather_data(url: str) -> dict:
    response = requests.get(url)
    if response.status_code != 200:
        error_message = response.json().get('message', 'City not found')
        raise HTTPException(status_code=response.status_code, detail=error_message)
    return response.json()


def get_weather(city: str, weather_api_key: str) -> dict:
    url = get_weather_url(city, weather_api_key)
    data = get_weather_data(url)
    return parse_weather_data(data)


@app.get("/weather/{city_name}")
def weather(city_name: str):
    weather = get_weather(city_name, weather_api_key)
    return weather
