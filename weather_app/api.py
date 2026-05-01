"""API client for fetching weather data."""
import urllib.request
import urllib.parse
import json
from typing import Optional, List

from .config import GEOCODING_API, WEATHER_API, WEATHER_CODES, TEMPERATURE_UNITS, PRESET_CITIES
from .models import Location, WeatherData, ForecastDay


def fetch_json(url: str) -> dict:
    """Fetch JSON data from a URL."""
    with urllib.request.urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode())


def get_location(city: str) -> Optional[Location]:
    """Get location — checks preset cities first, then geocoding API."""
    # Check preset cities first (instant, no API call)
    key = city.strip().lower()
    if key in PRESET_CITIES:
        p = PRESET_CITIES[key]
        return Location(
            name=p["name"],
            country=p["country"],
            latitude=p["latitude"],
            longitude=p["longitude"],
            timezone=p["timezone"],
        )

    # Fallback: geocoding API
    try:
        params = urllib.parse.urlencode({
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        })
        url = f"{GEOCODING_API}?{params}"
        data = fetch_json(url)
        results = data.get("results", [])
        if not results:
            return None
        r = results[0]
        return Location(
            name=r.get("name", city),
            country=r.get("country", "Unknown"),
            latitude=r["latitude"],
            longitude=r["longitude"],
            timezone=r.get("timezone", "UTC"),
        )
    except Exception:
        return None


def get_current_weather(location: Location, units: str = "metric") -> WeatherData:
    """Fetch current weather for a location."""
    temp_unit = "celsius" if units == "metric" else "fahrenheit"
    params = urllib.parse.urlencode({
        "latitude": location.latitude,
        "longitude": location.longitude,
        "current": "temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,wind_direction_10m,weather_code",
        "temperature_unit": temp_unit,
        "wind_speed_unit": "kmh",
        "timezone": location.timezone,
    })
    url = f"{WEATHER_API}?{params}"
    data = fetch_json(url)

    current = data["current"]
    code = current["weather_code"]
    condition, emoji = WEATHER_CODES.get(code, ("Unknown", "🌡️"))
    unit_symbol = TEMPERATURE_UNITS.get(units, "°C")

    return WeatherData(
        location=location,
        temperature=current["temperature_2m"],
        feels_like=current["apparent_temperature"],
        humidity=current["relative_humidity_2m"],
        wind_speed=current["wind_speed_10m"],
        wind_direction=current["wind_direction_10m"],
        weather_code=code,
        condition=condition,
        condition_emoji=emoji,
        units=unit_symbol,
    )


def get_forecast(location: Location, days: int = 7, units: str = "metric") -> List[ForecastDay]:
    """Fetch multi-day forecast for a location."""
    temp_unit = "celsius" if units == "metric" else "fahrenheit"
    params = urllib.parse.urlencode({
        "latitude": location.latitude,
        "longitude": location.longitude,
        "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum",
        "temperature_unit": temp_unit,
        "forecast_days": days,
        "timezone": location.timezone,
    })
    url = f"{WEATHER_API}?{params}"
    data = fetch_json(url)

    daily = data["daily"]
    unit_symbol = TEMPERATURE_UNITS.get(units, "°C")
    forecast = []

    for i, date in enumerate(daily["time"]):
        code = daily["weather_code"][i]
        condition, emoji = WEATHER_CODES.get(code, ("Unknown", "🌡️"))
        forecast.append(ForecastDay(
            date=date,
            max_temp=daily["temperature_2m_max"][i],
            min_temp=daily["temperature_2m_min"][i],
            weather_code=code,
            condition=condition,
            condition_emoji=emoji,
            precipitation_sum=daily["precipitation_sum"][i],
            units=unit_symbol,
        ))

    return forecast
