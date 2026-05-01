"""Flask web application for weather app."""
from flask import Flask, render_template, request, jsonify
import sys
import os

# Add the weather_app module to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'weather_app'))

from weather_app.api import get_location, get_current_weather, get_forecast
from weather_app.models import WeatherData, Location

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main weather page."""
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    """API endpoint to get weather data."""
    city = request.args.get('city', 'London')
    units = request.args.get('units', 'metric')
    forecast_days = int(request.args.get('forecast_days', 0))
    
    try:
        location = get_location(city)
        if not location:
            return jsonify({'error': f'City "{city}" not found'}), 404
        
        current_weather = get_current_weather(location, units)
        
        result = {
            'current': current_weather.to_dict(),
            'location': {
                'name': location.name,
                'country': location.country,
                'latitude': location.latitude,
                'longitude': location.longitude
            }
        }
        
        if forecast_days > 0:
            forecast = get_forecast(location, forecast_days, units)
            result['forecast'] = [
                {
                    'date': day.date,
                    'condition': f"{day.condition_emoji} {day.condition}",
                    'max_temp': f"{day.max_temp}{day.units}",
                    'min_temp': f"{day.min_temp}{day.units}",
                    'precipitation': f"{day.precipitation_sum}mm"
                }
                for day in forecast
            ]
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
