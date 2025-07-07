#!/usr/bin/env python3
"""
Weather Dashboard - Main Application
Author: Mindy Stricklin
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import Config
from utils.api_client import WeatherAPI
from features.weather_display import WeatherDisplay
from features.weather_history import WeatherHistory
from features.weather_alerts import WeatherAlerts
from features.weather_journal import WeatherJournal

class WeatherDashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weather Dashboard")
        self.root.geometry("800x600")
        
        # Initialize components
        self.config = Config()
        self.api = WeatherAPI(self.config.get_api_key())
        
        # Create main interface
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Weather Dashboard", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Location entry
        ttk.Label(main_frame, text="Enter City:").grid(row=1, column=0, sticky=tk.W)
        self.location_var = tk.StringVar()
        location_entry = ttk.Entry(main_frame, textvariable=self.location_var, width=30)
        location_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))
        
        # Get Weather button
        get_weather_btn = ttk.Button(main_frame, text="Get Weather", 
                                    command=self.get_weather)
        get_weather_btn.grid(row=1, column=2, padx=(10, 0))
        
        # Weather display area
        self.weather_text = tk.Text(main_frame, height=15, width=60)
        self.weather_text.grid(row=2, column=0, columnspan=3, pady=(20, 0))
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_label = ttk.Label(main_frame, textvariable=self.status_var)
        status_label.grid(row=3, column=0, columnspan=3, sticky=tk.W, pady=(10, 0))
        
    def get_weather(self):
        location = self.location_var.get().strip()
        if not location:
            messagebox.showerror("Error", "Please enter a city name")
            return
            
        try:
            self.status_var.set("Getting weather data...")
            self.root.update()
            
            # This is where we'll call the API
            # For now, just display a placeholder
            weather_info = f"Weather data for {location} will be displayed here.\n"
            weather_info += "This is a placeholder until API integration is complete."
            
            self.weather_text.delete(1.0, tk.END)
            self.weather_text.insert(1.0, weather_info)
            
            self.status_var.set("Weather data retrieved successfully")
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve weather data: {str(e)}")
            self.status_var.set("Error retrieving weather data")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WeatherDashboard()
    app.run()
