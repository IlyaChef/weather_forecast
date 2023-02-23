import requests
from fastapi import FastAPI
from config import WEATHER_API_KEY


app = FastAPI()


def get_weather(city: str) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=en"
    response = requests.get(url)
    data = response.json()
    return {
        "Temperature": data["main"]["temp"],
        "Feels like": data["main"]["feels_like"],
        "Description": data["weather"][0]["description"],
    }

@app.get("/weather/{city_name}")
def weather(city_name: str):
    weather = get_weather(city_name)
    return weather
