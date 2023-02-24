import requests
from fastapi import FastAPI
from dotenv import load_dotenv
from os import getenv


load_dotenv()

app = FastAPI()

WEATHER_API_KEY = getenv("WEATHER_API_KEY")


def get_weather(city: str) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=en"
    response = requests.get(url)
    data = response.json()
    return {
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "description": data["weather"][0]["description"],
    }

@app.get("/weather/{city_name}")
def weather(city_name: str):
    weather = get_weather(city_name)
    return weather
