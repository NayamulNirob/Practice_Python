import os
import requests
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Read the API key at request time to avoid issues with uvicorn's reloader
# (the parent reload process may have a different environment than worker).
# The key is read inside get_weather().

api_key = os.getenv("OPENWEATHER_API_KEY")


@app.get("/")
def home():
    return {
        "message": "Weather Forecast API is running"
    }


@app.get("/weather")
def get_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"

    if not api_key:
        raise HTTPException(status_code=500, detail="Server configuration error: OPENWEATHER_API_KEY not set")

    # Diagnostic: show masked key prefix and city (does not expose full key)
    print(f"Using OPENWEATHER_API_KEY prefix={api_key[:8]}..., city={city}")

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        try:
            error_text = response.text
        except Exception:
            error_text = "<no response body>"
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Could not get weather data: status={response.status_code}, body={error_text}"
        )

    data = response.json()

    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
    }


@app.get("/forecast")
def get_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/forecast"

    if not api_key:
        raise HTTPException(status_code=500, detail="Server configuration error: OPENWEATHER_API_KEY not set")

    # Diagnostic: show masked key prefix and city (does not expose full key)
    print(f"Using OPENWEATHER_API_KEY prefix={api_key[:8]}..., city={city}")

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        try:
            error_text = response.text
        except Exception:
            error_text = "<no response body>"
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Could not get weather data: status={response.status_code}, body={error_text}"
        )

    data = response.json()

    return {
        "city": data["city"]["name"],
        "forecast": data["list"]
    }