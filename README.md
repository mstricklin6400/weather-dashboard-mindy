# Weather Dashboard

A Python-based weather dashboard application that provides current weather information, tracks weather history, and includes personal weather journaling features.

## Features

### Core Features
1. **Current Weather Display** - Get real-time weather information for any city
2. **Weather History Tracking** - Keep track of weather patterns over time
3. **Weather Alerts System** - Get notified when weather conditions meet your criteria

### Enhancement
- **Weather Journal** - Record your daily mood and notes alongside weather data

## Project Structure

```
weather-dashboard-mindy/
├── main.py                 # Main application entry point
├── config.py              # Configuration settings
├── .env                   # Environment variables (API keys)
├── data/                  # Data storage
│   ├── weather_history.txt
│   ├── journal_entries.json
│   └── alert_preferences.json
├── features/              # Feature modules
│   ├── weather_display.py
│   ├── weather_history.py
│   ├── weather_alerts.py
│   └── weather_journal.py
├── utils/                 # Utility functions
│   ├── api_client.py
│   └── data_manager.py
└── docs/                  # Documentation
    └── Week11_Reflection.md
```

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- OpenWeatherMap API key (free at https://openweathermap.org/api)

### Installation
1. Clone this repository
2. Install required packages:
   ```bash
   pip install requests python-dotenv
   ```
3. Create a `.env` file in the project root:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Usage

### Getting Weather Information
1. Enter a city name in the input field
2. Click "Get Weather" to fetch current conditions
3. Weather data will be displayed and automatically saved to history

### Setting Up Alerts
- Temperature alerts trigger when temperatures exceed your set thresholds
- Condition alerts notify you of specific weather conditions (rain, snow, etc.)
- Alert preferences are saved in `data/alert_preferences.json`

### Using the Weather Journal
- Add daily mood and notes alongside weather data
- View historical entries to track patterns
- Search through past entries

## Data Files

### weather_history.txt
Stores weather data in CSV format:
```
2025-07-07,New Brunswick,NJ,75,Partly Cloudy,1015.2
```

### journal_entries.json
Stores personal journal entries:
```json
{
  "date": "2025-07-07",
  "mood": "Happy",
  "notes": "Beautiful weather today!",
  "weather_data": {...}
}
```

### alert_preferences.json
Stores user alert preferences:
```json
{
  "temperature_threshold_high": 85,
  "temperature_threshold_low": 32,
  "condition_alerts": ["rain", "snow"],
  "enabled": true
}
```

## Development Status

This project is currently in development as part of a Python capstone project. 

**Current Status:** Week 11 - Planning and Setup Phase
**Next Steps:** API integration and basic GUI implementation

## API Usage

This application uses the OpenWeatherMap API for weather data. Please be mindful of rate limits:
- Free tier: 1000 calls/month, 60 calls/minute
- The app implements automatic rate limiting to prevent exceeding limits

## Contributing

This is a student project, but feedback and suggestions are welcome!

## License

This project is for educational purposes. Weather data provided by OpenWeatherMap.

---

*Author: Mindy Stricklin*  
*Project: Weather Dashboard Capstone*  
*Date: July 2025*