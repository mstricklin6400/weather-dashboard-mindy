"""
Feature: Weather History
- Tracks and stores weather data over time
Author: Mindy Stricklin
"""

import os
from datetime import datetime

class WeatherHistory:
    def __init__(self, data_folder='data'):
        self.data_folder = data_folder
        self.history_file = os.path.join(data_folder, 'weather_history.txt')
        self.ensure_data_folder()
    
    def ensure_data_folder(self):
        """Create data folder if it doesn't exist"""
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
    
    def add_weather_record(self, city, state, temp, condition, pressure=None):
        """
        Add a weather record to the history file
        Format: date,city,state,temp,condition,pressure
        """
        try:
            date_str = datetime.now().strftime('%Y-%m-%d')
            pressure_str = str(pressure) if pressure else 'N/A'
            
            record = f"{date_str},{city},{state},{temp},{condition},{pressure_str}\n"
            
            with open(self.history_file, 'a') as f:
                f.write(record)
            
            return True
            
        except Exception as e:
            print(f"Error adding weather record: {str(e)}")
            return False
    
    def get_recent_history(self, days=7):
        """
        Get weather history for the last N days
        """
        try:
            if not os.path.exists(self.history_file):
                return []
            
            history = []
            with open(self.history_file, 'r') as f:
                lines = f.readlines()
                # Get the last 'days' number of lines
                recent_lines = lines[-days:] if len(lines) > days else lines
                
                for line in recent_lines:
                    line = line.strip()
                    if line:
                        parts = line.split(',')
                        if len(parts) >= 5:
                            history.append({
                                'date': parts[0],
                                'city': parts[1],
                                'state': parts[2],
                                'temp': parts[3],
                                'condition': parts[4],
                                'pressure': parts[5] if len(parts) > 5 else 'N/A'
                            })
            
            return history
            
        except Exception as e:
            print(f"Error reading weather history: {str(e)}")
            return []
    
    def get_history_summary(self):
        """
        Get a summary of weather history
        """
        history = self.get_recent_history(30)  # Last 30 days
        
        if not history:
            return "No weather history available"
        
        total_records = len(history)
        
        # Calculate average temperature
        temps = [float(record['temp']) for record in history if record['temp'].replace('.', '').isdigit()]
        avg_temp = sum(temps) / len(temps) if temps else 0
        
        # Count conditions
        conditions = {}
        for record in history:
            condition = record['condition']
            conditions[condition] = conditions.get(condition, 0) + 1
        
        most_common_condition = max(conditions, key=conditions.get) if conditions else "Unknown"
        
        summary = f"""
Weather History Summary (Last {total_records} records):
Average Temperature: {avg_temp:.1f}°F
Most Common Condition: {most_common_condition}
Total Records: {total_records}
        """
        
        return summary.strip()
    
    def clear_history(self):
        """
        Clear all weather history (use with caution!)
        """
        try:
            if os.path.exists(self.history_file):
                os.remove(self.history_file)
            return True
        except Exception as e:
            print(f"Error clearing history: {str(e)}")
            return False
