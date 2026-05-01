"""Command-line interface for Weather App."""
import argparse
import sys

from .config import DEFAULT_CITY, DEFAULT_UNITS
from .api import get_location, get_current_weather, get_forecast
from .display import print_current_weather, print_forecast, print_error


def parse_args():
    parser = argparse.ArgumentParser(
        description="🌤️  Weather CLI App - Get weather info from the terminal",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m weather_app London
  python -m weather_app "New York" --units imperial
  python -m weather_app Tokyo --forecast
  python -m weather_app Mumbai --forecast --days 3
        """
    )
    parser.add_argument(
        "city",
        nargs="?",
        default=DEFAULT_CITY,
        help=f"City name (default: {DEFAULT_CITY})"
    )
    parser.add_argument(
        "--units",
        choices=["metric", "imperial", "standard"],
        default=DEFAULT_UNITS,
        help="Temperature units (default: metric)"
    )
    parser.add_argument(
        "--forecast",
        action="store_true",
        help="Show 7-day forecast"
    )
    parser.add_argument(
        "--days",
        type=int,
        default=7,
        choices=range(1, 8),
        metavar="[1-7]",
        help="Number of forecast days (default: 7)"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    print(f"\n  🔍  Fetching weather for '{args.city}'...")

    location = get_location(args.city)
    if not location:
        print_error(f"City '{args.city}' not found. Please check the spelling.")
        sys.exit(1)

    weather = get_current_weather(location, units=args.units)
    print_current_weather(weather)

    if args.forecast:
        forecast = get_forecast(location, days=args.days, units=args.units)
        print_forecast(forecast)

    print()


if __name__ == "__main__":
    main()
