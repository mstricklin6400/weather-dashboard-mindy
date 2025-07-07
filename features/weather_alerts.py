"""
Feature: Weather Alerts
- Provides weather alerts based on user preferences
Author: Mindy Stricklin
"""

import json
import os
from datetime import datetime

class WeatherAlerts:
    def __init__(self, data_folder='data'):
        self.data_folder = data_folder
        self.alerts_file = os.path.join(data_folder, 'alert_preferences.json')
        self.default_preferences = {
            'temperature_threshold_high': 85,
            'temperature_threshold_low': 32,
            'condition_alerts': ['rain', 'snow', 'thunderstorm'],
            'enabled': True
        }
        self.ensure_data_folder()
        self.load_preferences()
    
    def ensure_data_folder(self):
        """Create data folder if it doesn't exist"""
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
    
    def load_preferences(self):
        """Load alert preferences from file"""
        try:
            if os.path.exists(self.alerts_file):
                with open(self.alerts_file, 'r') as f:
                    self.preferences = json.load(f)
            else:
                self.preferences = self.default_preferences.copy()
                self.save_preferences()
        except Exception as e:
            print(f"Error loading alert preferences: {str(e)}")
            self.preferences = self.default_preferences.copy()
    
    def save_preferences(self):
        """Save alert preferences to file"""
        try:
            with open(self.alerts_file, 'w') as f:
                json.dump(self.preferences, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving alert preferences: {str(e)}")
            return False
    
    def check_alerts(self, temp, condition):
        """
        Check if current weather conditions trigger any alerts
        Returns a list of alert messages
        """
        alerts = []
        
        if not self.preferences.get('enabled', True):
            return alerts
        
        # Temperature alerts
        high_temp = self.preferences.get('temperature_threshold_high', 85)
        low_temp = self.preferences.get('temperature_threshold_low', 32)
        
        try:
            temp_float = float(temp)
            if temp_float >= high_temp:
                alerts.append(f"🔥 High Temperature Alert: {temp}°F (threshold: {high_temp}°F)")
            elif temp_float <= low_temp:
                alerts.append(f"❄️ Low Temperature Alert: {temp}°F (threshold: {low_temp}°F)")
        except ValueError:
            pass
        
        # Condition alerts
        condition_alerts = self.preferences.get('condition_alerts', [])
        condition_lower = condition.lower()
        
        for alert_condition in condition_alerts:
            if alert_condition.lower() in condition_lower:
                alerts.append(f"⚠️ Weather Alert: {condition} detected")
        
        return alerts
    
    def set_temperature_thresholds(self, high_temp, low_temp):
        """Set temperature alert thresholds"""
        self.preferences['temperature_threshold_high'] = high_temp
        self.preferences['temperature_threshold_low'] = low_temp
        return self.save_preferences()
    
    def set_condition_alerts(self, conditions):
        """Set which weather conditions trigger alerts"""
        if isinstance(conditions, list):
            self.preferences['condition_alerts'] = conditions
            return self.save_preferences()
        return False
    
    def toggle_alerts(self, enabled=None):
        """Enable or disable all alerts"""
        if enabled is None:
            enabled = not self.preferences.get('enabled', True)
        
        self.preferences['enabled'] = enabled
        return self.save_preferences()
    
    def get_preferences_summary(self):
        """Get a summary of current alert preferences"""
        enabled = self.preferences.get('enabled', True)
        high_temp = self.preferences.get('temperature_threshold_high', 85)
        low_temp = self.preferences.get('temperature_threshold_low', 32)
        conditions = self.preferences.get('condition_alerts', [])
        
        summary = f"""
Alert Preferences:
Status: {'Enabled' if enabled else 'Disabled'}
High Temperature Alert: {high_temp}°F
Low Temperature Alert: {low_temp}°F
Condition Alerts: {', '.join(conditions) if conditions else 'None'}
        """
        
        return summary.strip()
    
    def test_alerts(self):
        """Test the alert system with sample data"""
        test_cases = [
            (90, "Sunny"),
            (25, "Snow"),
            (72, "Thunderstorm"),
            (60, "Clear")
        ]
        
        print("Testing alert system:")
        for temp, condition in test_cases:
            alerts = self.check_alerts(temp, condition)
            print(f"  {temp}°F, {condition}: {len(alerts)} alerts")
            for alert in alerts:
                print(f"    {alert}")
        
        return True
