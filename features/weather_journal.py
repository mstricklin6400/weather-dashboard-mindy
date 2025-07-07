"""
Feature: Weather Journal
- Stores daily mood and notes alongside weather data
Author: Mindy Stricklin
"""

import json
import os
from datetime import datetime

class WeatherJournal:
    def __init__(self, data_folder='data'):
        self.data_folder = data_folder
        self.journal_file = os.path.join(data_folder, 'journal_entries.json')
        self.ensure_data_folder()
    
    def ensure_data_folder(self):
        """Create data folder if it doesn't exist"""
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
    
    def add_journal_entry(self, date, mood, notes, weather_data=None):
        """
        Add a journal entry with weather and mood data
        """
        try:
            # Load existing entries
            entries = self.load_entries()
            
            # Create new entry
            entry = {
                'date': date,
                'mood': mood,
                'notes': notes,
                'timestamp': datetime.now().isoformat(),
                'weather_data': weather_data
            }
            
            # Add to entries
            entries.append(entry)
            
            # Save back to file
            return self.save_entries(entries)
            
        except Exception as e:
            print(f"Error adding journal entry: {str(e)}")
            return False
    
    def load_entries(self):
        """Load all journal entries from file"""
        try:
            if os.path.exists(self.journal_file):
                with open(self.journal_file, 'r') as f:
                    return json.load(f)
            else:
                return []
        except Exception as e:
            print(f"Error loading journal entries: {str(e)}")
            return []
    
    def save_entries(self, entries):
        """Save journal entries to file"""
        try:
            with open(self.journal_file, 'w') as f:
                json.dump(entries, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving journal entries: {str(e)}")
            return False
    
    def get_recent_entries(self, days=7):
        """Get journal entries from the last N days"""
        entries = self.load_entries()
        
        if not entries:
            return []
        
        # Sort by date and get recent entries
        sorted_entries = sorted(entries, key=lambda x: x['date'], reverse=True)
        return sorted_entries[:days]
    
    def get_entry_by_date(self, date):
        """Get journal entry for a specific date"""
        entries = self.load_entries()
        
        for entry in entries:
            if entry['date'] == date:
                return entry
        
        return None
    
    def update_entry(self, date, mood=None, notes=None):
        """Update an existing journal entry"""
        try:
            entries = self.load_entries()
            
            for entry in entries:
                if entry['date'] == date:
                    if mood is not None:
                        entry['mood'] = mood
                    if notes is not None:
                        entry['notes'] = notes
                    entry['last_updated'] = datetime.now().isoformat()
                    
                    return self.save_entries(entries)
            
            return False  # Entry not found
            
        except Exception as e:
            print(f"Error updating journal entry: {str(e)}")
            return False
    
    def delete_entry(self, date):
        """Delete a journal entry by date"""
        try:
            entries = self.load_entries()
            
            # Filter out the entry to delete
            updated_entries = [entry for entry in entries if entry['date'] != date]
            
            if len(updated_entries) < len(entries):
                return self.save_entries(updated_entries)
            else:
                return False  # Entry not found
                
        except Exception as e:
            print(f"Error deleting journal entry: {str(e)}")
            return False
    
    def get_mood_summary(self):
        """Get a summary of mood patterns"""
        entries = self.load_entries()
        
        if not entries:
            return "No journal entries available"
        
        # Count moods
        mood_counts = {}
        for entry in entries:
            mood = entry.get('mood', 'Unknown')
            mood_counts[mood] = mood_counts.get(mood, 0) + 1
        
        # Find most common mood
        most_common_mood = max(mood_counts, key=mood_counts.get) if mood_counts else "Unknown"
        
        total_entries = len(entries)
        
        summary = f"""
Journal Summary:
Total Entries: {total_entries}
Most Common Mood: {most_common_mood}
Mood Distribution:
"""
        
        for mood, count in mood_counts.items():
            percentage = (count / total_entries) * 100
            summary += f"  {mood}: {count} entries ({percentage:.1f}%)\n"
        
        return summary.strip()
    
    def search_entries(self, keyword):
        """Search journal entries for a keyword"""
        entries = self.load_entries()
        matching_entries = []
        
        keyword_lower = keyword.lower()
        
        for entry in entries:
            # Search in notes
            if keyword_lower in entry.get('notes', '').lower():
                matching_entries.append(entry)
            # Search in mood
            elif keyword_lower in entry.get('mood', '').lower():
                matching_entries.append(entry)
        
        return matching_entries
