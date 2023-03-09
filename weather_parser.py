def parse_weather_data(data: dict[str, float]) -> dict[str, float]:
    return {
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "description": data["weather"][0]["description"],
    }
