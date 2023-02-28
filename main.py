from fastapi import FastAPI
from openweather_api import get_weather
from openweather_api import weather_api_key


app = FastAPI()


@app.get("/weather/{city_name}")
def weather(city_name: str):
    weather = get_weather(city_name, weather_api_key)
    return weather
