"""
API Client for OpenWeatherMap
Author: Mindy Stricklin
"""

import requests
import json
import time
from datetime import datetime, timedelta

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"
        self.last_request_time = 0
        self.rate_limit_delay = 1  # seconds between requests
    
    def _make_request(self, endpoint, params):
        """Make a rate-limited request to the API"""
        # Rate limiting
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < self.rate_limit_delay:
            time.sleep(self.rate_limit_delay - time_since_last)
        
        try:
            url = f"{self.base_url}/{endpoint}"
            params['appid'] = self.api_key
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            self.last_request_time = time.time()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON response from API")
    
    def get_current_weather(self, city, units='imperial'):
        """Get current weather for a city"""
        params = {
            'q': city,
            'units': units
        }
        
        return self._make_request('weather', params)
    
    def get_weather_by_coords(self, lat, lon, units='imperial'):
        """Get weather by coordinates"""
        params = {
            'lat': lat,
            'lon': lon,
            'units': units
        }
        
        return self._make_request('weather', params)
    
    def get_forecast(self, city, units='imperial'):
        """Get 5-day forecast for a city"""
        params = {
            'q': city,
            'units': units
        }
        
        return self._make_request('forecast', params)
    
    def test_connection(self):
        """Test if API connection is working"""
        try:
            data = self.get_current_weather('London')
            return True, "API connection successful"
        except Exception as e:
            return False, str(e)
    
    def parse_weather_data(self, data):
        """Parse weather data into a standardized format"""
        try:
            parsed = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'],
                'condition': data['weather'][0]['main'],
                'timestamp': datetime.now().isoformat()
            }
            return parsed
        except KeyError as e:
            raise Exception(f"Error parsing weather data: missing key {str(e)}")
    
    def get_weather_summary(self, city):
        """Get a formatted weather summary"""
        try:
            data = self.get_current_weather(city)
            parsed = self.parse_weather_data(data)
            
            summary = f"""
Weather Summary for {parsed['city']}, {parsed['country']}:
Temperature: {parsed['temperature']}°F (feels like {parsed['feels_like']}°F)
Condition: {parsed['description'].title()}
Humidity: {parsed['humidity']}%
Pressure: {parsed['pressure']} hPa
Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            """
            
            return summary.strip(), parsed
            
        except Exception as e:
            return f"Error getting weather summary: {str(e)}", None
