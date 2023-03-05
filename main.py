from fastapi import FastAPI
from openweather_api import get_weather


app = FastAPI()


@app.get("/weather/{city_name}")
def weather(city_name: str):
    weather = get_weather(city_name)
    return weather
