"""Tests for data models."""
import unittest
from weather_app.models import Location, WeatherData, ForecastDay


class TestLocation(unittest.TestCase):
    def setUp(self):
        self.location = Location(
            name="London",
            country="United Kingdom",
            latitude=51.5074,
            longitude=-0.1278,
            timezone="Europe/London"
        )

    def test_str(self):
        self.assertEqual(str(self.location), "London, United Kingdom")


class TestWeatherData(unittest.TestCase):
    def setUp(self):
        loc = Location("London", "UK", 51.5, -0.1, "Europe/London")
        self.weather = WeatherData(
            location=loc,
            temperature=18.5,
            feels_like=17.0,
            humidity=72,
            wind_speed=15.0,
            wind_direction=270,
            weather_code=1,
            condition="Mainly Clear",
            condition_emoji="🌤️",
            units="°C"
        )

    def test_wind_direction_label(self):
        self.assertEqual(self.weather.wind_direction_label(), "W")

    def test_to_dict(self):
        d = self.weather.to_dict()
        self.assertIn("temperature", d)
        self.assertIn("humidity", d)
        self.assertEqual(d["temperature"], "18.5°C")


class TestForecastDay(unittest.TestCase):
    def test_str(self):
        day = ForecastDay(
            date="2024-06-01",
            max_temp=22.0,
            min_temp=14.0,
            weather_code=0,
            condition="Clear Sky",
            condition_emoji="☀️",
            precipitation_sum=0.0,
            units="°C"
        )
        result = str(day)
        self.assertIn("2024-06-01", result)
        self.assertIn("22.0", result)


if __name__ == "__main__":
    unittest.main()
