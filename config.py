"""
Configuration settings for Weather Dashboard
Author: Mindy Stricklin
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for the weather dashboard application"""
    
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.base_url = 'https://api.openweathermap.org/data/2.5'
        self.units = 'imperial'  # fahrenheit, mph, etc.
        self.data_folder = 'data'
        self.history_file = 'weather_history.txt'
        self.journal_file = 'journal_entries.json'
        self.alerts_file = 'alert_preferences.json'
        
    def get_api_key(self):
        """Get the OpenWeatherMap API key"""
        if not self.api_key:
            raise ValueError("OpenWeatherMap API key not found. Please add OPENWEATHER_API_KEY to your .env file")
        return self.api_key
    
    def get_api_url(self, endpoint):
        """Get the full API URL for a given endpoint"""
        return f"{self.base_url}/{endpoint}"
    
    def get_data_file_path(self, filename):
        """Get the full path to a data file"""
        return os.path.join(self.data_folder, filename)
    
    def get_history_file_path(self):
        """Get the full path to the weather history file"""
        return self.get_data_file_path(self.history_file)
    
    def get_journal_file_path(self):
        """Get the full path to the journal file"""
        return self.get_data_file_path(self.journal_file)
    
    def get_alerts_file_path(self):
        """Get the full path to the alerts preferences file"""
        return self.get_data_file_path(self.alerts_file)
