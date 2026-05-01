"""Data models for Weather App."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Location:
    """Represents a geographic location."""
    name: str
    country: str
    latitude: float
    longitude: float
    timezone: str

    def __str__(self):
        return f"{self.name}, {self.country}"


@dataclass
class WeatherData:
    """Represents current weather data."""
    location: Location
    temperature: float
    feels_like: float
    humidity: int
    wind_speed: float
    wind_direction: int
    weather_code: int
    condition: str
    condition_emoji: str
    units: str

    def wind_direction_label(self) -> str:
        """Convert degrees to compass direction."""
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        index = round(self.wind_direction / 45) % 8
        return directions[index]

    def to_dict(self) -> dict:
        return {
            "city": str(self.location),
            "temperature": f"{self.temperature}{self.units}",
            "feels_like": f"{self.feels_like}{self.units}",
            "humidity": f"{self.humidity}%",
            "wind": f"{self.wind_speed} km/h {self.wind_direction_label()}",
            "condition": f"{self.condition_emoji} {self.condition}",
        }


@dataclass
class ForecastDay:
    """Represents a single day forecast."""
    date: str
    max_temp: float
    min_temp: float
    weather_code: int
    condition: str
    condition_emoji: str
    precipitation_sum: float
    units: str

    def __str__(self):
        return (
            f"{self.date}: {self.condition_emoji} {self.condition} | "
            f"High: {self.max_temp}{self.units} | Low: {self.min_temp}{self.units} | "
            f"Rain: {self.precipitation_sum}mm"
        )
