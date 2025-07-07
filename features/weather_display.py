"""
Feature: Weather Display
- Fetches and displays current weather information
Author: Mindy Stricklin
"""

import requests
import json
from datetime import datetime

class WeatherDisplay:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def get_current_weather(self, city):
        """
        Get current weather for a given city
        """
        try:
            # API call parameters
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'imperial'
            }
            
            # Make API request
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            # Parse JSON response
            data = response.json()
            
            # Format weather information
            weather_info = self.format_weather_data(data)
            return weather_info
            
        except requests.exceptions.RequestException as e:
            return f"Error fetching weather data: {str(e)}"
        except json.JSONDecodeError:
            return "Error parsing weather data"
    
    def format_weather_data(self, data):
        """
        Format raw weather data into readable string
        """
        try:
            city = data['name']
            country = data['sys']['country']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description'].title()
            
            formatted_data = f"""
Current Weather for {city}, {country}:
Temperature: {temp}°F (Feels like {feels_like}°F)
Condition: {description}
Humidity: {humidity}%
Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            """
            
            return formatted_data.strip()
            
        except KeyError as e:
            return f"Error formatting weather data: Missing key {str(e)}"
    
    def is_api_key_valid(self):
        """
        Check if the API key is valid by making a test request
        """
        try:
            test_params = {
                'q': 'London',
                'appid': self.api_key,
                'units': 'imperial'
            }
            response = requests.get(self.base_url, params=test_params)
            return response.status_code == 200
        except:
            return False
