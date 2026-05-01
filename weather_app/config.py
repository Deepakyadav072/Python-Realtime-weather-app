"""Configuration settings for the Weather App."""

# Default settings
DEFAULT_CITY = "Lucknow"
DEFAULT_UNITS = "metric"  # 'metric' for Celsius, 'imperial' for Fahrenheit
TEMPERATURE_UNITS = {
    "metric": "°C",
    "imperial": "°F",
    "standard": "K"
}

# API endpoint (uses Open-Meteo - free, no API key required)
GEOCODING_API = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_API = "https://api.open-meteo.com/v1/forecast"

# Preset cities with hardcoded coordinates (instant lookup, no API call needed)
PRESET_CITIES = {
    "lucknow": {
        "name": "Lucknow",
        "country": "India",
        "latitude": 26.8467,
        "longitude": 80.9462,
        "timezone": "Asia/Kolkata",
    },
    "delhi": {
        "name": "Delhi",
        "country": "India",
        "latitude": 28.6139,
        "longitude": 77.2090,
        "timezone": "Asia/Kolkata",
    },
    "mumbai": {
        "name": "Mumbai",
        "country": "India",
        "latitude": 19.0760,
        "longitude": 72.8777,
        "timezone": "Asia/Kolkata",
    },
    "bangalore": {
        "name": "Bangalore",
        "country": "India",
        "latitude": 12.9716,
        "longitude": 77.5946,
        "timezone": "Asia/Kolkata",
    },
    "kolkata": {
        "name": "Kolkata",
        "country": "India",
        "latitude": 22.5726,
        "longitude": 88.3639,
        "timezone": "Asia/Kolkata",
    },
    "london": {
        "name": "London",
        "country": "United Kingdom",
        "latitude": 51.5074,
        "longitude": -0.1278,
        "timezone": "Europe/London",
    },
    "new york": {
        "name": "New York",
        "country": "United States",
        "latitude": 40.7128,
        "longitude": -74.0060,
        "timezone": "America/New_York",
    },
    "tokyo": {
        "name": "Tokyo",
        "country": "Japan",
        "latitude": 35.6762,
        "longitude": 139.6503,
        "timezone": "Asia/Tokyo",
    },
    "paris": {
        "name": "Paris",
        "country": "France",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris",
    },
    "dubai": {
        "name": "Dubai",
        "country": "UAE",
        "latitude": 25.2048,
        "longitude": 55.2708,
        "timezone": "Asia/Dubai",
    },
}

# Weather condition codes mapping
WEATHER_CODES = {
    0: ("Clear Sky", "☀️"),
    1: ("Mainly Clear", "🌤️"),
    2: ("Partly Cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Foggy", "🌫️"),
    48: ("Icy Fog", "🌫️"),
    51: ("Light Drizzle", "🌦️"),
    53: ("Moderate Drizzle", "🌦️"),
    55: ("Heavy Drizzle", "🌧️"),
    61: ("Slight Rain", "🌧️"),
    63: ("Moderate Rain", "🌧️"),
    65: ("Heavy Rain", "🌧️"),
    71: ("Slight Snow", "🌨️"),
    73: ("Moderate Snow", "❄️"),
    75: ("Heavy Snow", "❄️"),
    80: ("Slight Showers", "🌦️"),
    81: ("Moderate Showers", "🌧️"),
    82: ("Heavy Showers", "⛈️"),
    95: ("Thunderstorm", "⛈️"),
    99: ("Thunderstorm with Hail", "⛈️"),
}
