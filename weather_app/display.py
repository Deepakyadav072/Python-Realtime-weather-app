"""Display helpers for Weather App."""
from .models import WeatherData, ForecastDay
from typing import List


def print_separator(char="─", width=50):
    print(char * width)


def print_current_weather(weather: WeatherData):
    """Pretty-print current weather."""
    print_separator("═")
    print(f"  🌍 Weather for {weather.location}")
    print_separator("═")
    print(f"  {weather.condition_emoji}  {weather.condition}")
    print(f"  🌡️  Temperature  : {weather.temperature}{weather.units}")
    print(f"  🤔  Feels Like   : {weather.feels_like}{weather.units}")
    print(f"  💧  Humidity     : {weather.humidity}%")
    print(f"  💨  Wind         : {weather.wind_speed} km/h {weather.wind_direction_label()}")
    print_separator("─")


def print_forecast(forecast: List[ForecastDay]):
    """Pretty-print forecast."""
    print("\n  📅  7-Day Forecast")
    print_separator("─")
    for day in forecast:
        print(f"  {day}")
    print_separator("═")


def print_error(message: str):
    print(f"\n  ❌  Error: {message}\n")
