# 🌤️ Weather App

A Python weather app with both CLI and web interfaces to get real-time weather and forecasts — no API key required!

![image alt](https://github.com/Deepakyadav072/Python-Realtime-weather-app/blob/78a71961295a2df291c13622554534ba604f3ae0/weather.png)



## Features

- 🌍 Current weather for any city worldwide
- 📅 Up to 7-day forecast
- 🌡️ Metric, imperial, or standard units
- 💨 Wind speed & direction
- 💧 Humidity data
- 🌐 Modern web interface with responsive design
- 📱 Mobile-friendly UI with beautiful animations
- 🎨 Glass morphism design with gradient backgrounds

## Installation

### CLI Version
No installation needed! Just have Python 3.7+ installed.

### Web Version
Requires Flask for the web interface:

```bash
pip install flask
```

Then navigate to the project:

```bash
cd weather_app_project
```

## Usage

### CLI Version

```bash
# Basic usage (defaults to London)
python -m weather_app

# Specify a city
python -m weather_app Tokyo

# Imperial units (Fahrenheit)
python -m weather_app "New York" --units imperial

# Show 7-day forecast
python -m weather_app Paris --forecast

# Show 3-day forecast
python -m weather_app Mumbai --forecast --days 3
```

### Web Version

```bash
# Start the web server
python web_app.py

# Then open your browser and navigate to:
http://localhost:5000
```

**Web Interface Features:**
- 🎨 Modern, responsive design with glass morphism effects
- 🔍 Interactive city search with real-time results
- 🌡️ Toggle between Metric (°C) and Imperial (°F) units
- 📅 Optional 3, 5, or 7-day weather forecast
- 📱 Mobile-friendly interface that works on all devices
- ⚡ Smooth animations and transitions
- 🌍 Weather data with visual icons and descriptions

## Example Output

```
  🔍  Fetching weather for 'London'...
══════════════════════════════════════════════════
  🌍 Weather for London, United Kingdom
══════════════════════════════════════════════════
  🌤️  Mainly Clear
  🌡️  Temperature  : 18.5°C
  🤔  Feels Like   : 17.0°C
  💧  Humidity     : 72%
  💨  Wind         : 15.0 km/h W
──────────────────────────────────────────────────
```

## Running Tests

```bash
python -m unittest discover tests
```

## Project Structure

```
weather_app_project/
├── weather_app/
│   ├── __init__.py      # Package metadata
│   ├── __main__.py      # Entry point (python -m weather_app)
│   ├── cli.py           # Argument parsing & main flow
│   ├── api.py           # HTTP requests & data fetching
│   ├── models.py        # Data classes
│   ├── config.py        # Settings & constants
│   ├── display.py       # Terminal output formatting
│   ├── web_app.py       # Flask web application
│   └── templates/
│       └── index.html   # Web interface HTML template
├── tests/
│   ├── test_models.py
│   └── test_config.py
└── README.md
```

## Data Source

Uses [Open-Meteo](https://open-meteo.com/) — a free, open-source weather API. No API key needed!
