"""Tests for configuration."""
import unittest
from weather_app.config import WEATHER_CODES, TEMPERATURE_UNITS


class TestConfig(unittest.TestCase):
    def test_weather_codes_have_tuples(self):
        for code, value in WEATHER_CODES.items():
            self.assertIsInstance(value, tuple)
            self.assertEqual(len(value), 2)

    def test_temperature_units(self):
        self.assertIn("metric", TEMPERATURE_UNITS)
        self.assertIn("imperial", TEMPERATURE_UNITS)
        self.assertEqual(TEMPERATURE_UNITS["metric"], "°C")
        self.assertEqual(TEMPERATURE_UNITS["imperial"], "°F")


if __name__ == "__main__":
    unittest.main()
