from flask import Flask, render_template, request
import requests
import var
import os
from werkzeug.serving import run_simple

app = Flask(__name__)

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def get_forecast(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast data: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    forecast_data = None
    error_message = None

    if request.method == 'POST':
        city = request.form['city']
        if not city:
            error_message = "City name cannot be empty."
        else:
            api_key = var.key
            weather_data = get_weather(api_key, city)
            if weather_data:
                forecast_data = get_forecast(api_key, city)
            else:
                error_message = "Could not fetch weather data. Please check the city name and try again."

    return render_template('index.html', weather_data=weather_data, forecast_data=forecast_data, error_message=error_message)

if __name__ == "__main__":
    run_simple('0.0.0.0', int(os.environ.get("PORT", 8080)), app, use_debugger=True)