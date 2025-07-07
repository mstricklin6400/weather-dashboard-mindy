"""
Data Management utilities for Weather Dashboard
Author: Mindy Stricklin
"""

import os
import json
import csv
from datetime import datetime
import shutil

class DataManager:
    def __init__(self, data_folder='data'):
        self.data_folder = data_folder
        self.ensure_data_folder()
    
    def ensure_data_folder(self):
        """Create data folder if it doesn't exist"""
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
    
    def backup_data(self):
        """Create a backup of all data files"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_folder = f"{self.data_folder}_backup_{timestamp}"
            
            shutil.copytree(self.data_folder, backup_folder)
            return True, f"Backup created: {backup_folder}"
            
        except Exception as e:
            return False, f"Backup failed: {str(e)}"
    
    def validate_json_file(self, file_path):
        """Validate if a JSON file is properly formatted"""
        try:
            with open(file_path, 'r') as f:
                json.load(f)
            return True, "JSON file is valid"
        except json.JSONDecodeError as e:
            return False, f"JSON error: {str(e)}"
        except FileNotFoundError:
            return False, "File not found"
    
    def validate_csv_file(self, file_path):
        """Validate if a CSV file is properly formatted"""
        try:
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                row_count = sum(1 for row in reader)
            return True, f"CSV file is valid ({row_count} rows)"
        except Exception as e:
            return False, f"CSV error: {str(e)}"
    
    def get_file_stats(self, file_path):
        """Get statistics about a data file"""
        try:
            if not os.path.exists(file_path):
                return None
            
            stat = os.stat(file_path)
            
            return {
                'size_bytes': stat.st_size,
                'size_readable': self.format_file_size(stat.st_size),
                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                'created': datetime.fromtimestamp(stat.st_ctime).isoformat()
            }
        except Exception as e:
            return None
    
    def format_file_size(self, size_bytes):
        """Format file size in human-readable format"""
        if size_bytes == 0:
            return "0 B"
        
        size_names = ["B", "KB", "MB", "GB"]
        i = 0
        while size_bytes >= 1024 and i < len(size_names) - 1:
            size_bytes /= 1024
            i += 1
        
        return f"{size_bytes:.1f} {size_names[i]}"
    
    def clean_old_backups(self, keep_count=5):
        """Clean up old backup folders, keeping only the most recent ones"""
        try:
            # Find all backup folders
            backup_folders = []
            for item in os.listdir('.'):
                if item.startswith(f"{self.data_folder}_backup_") and os.path.isdir(item):
                    backup_folders.append(item)
            
            # Sort by name (which includes timestamp)
            backup_folders.sort(reverse=True)
            
            # Remove old backups
            removed_count = 0
            for folder in backup_folders[keep_count:]:
                try:
                    shutil.rmtree(folder)
                    removed_count += 1
                except Exception as e:
                    print(f"Error removing backup {folder}: {str(e)}")
            
            return removed_count
            
        except Exception as e:
            print(f"Error cleaning backups: {str(e)}")
            return 0
    
    def export_data_summary(self):
        """Export a summary of all data files"""
        summary = {
            'generated_at': datetime.now().isoformat(),
            'data_folder': self.data_folder,
            'files': {}
        }
        
        # Check each expected file
        expected_files = [
            'weather_history.txt',
            'journal_entries.json',
            'alert_preferences.json'
        ]
        
        for filename in expected_files:
            file_path = os.path.join(self.data_folder, filename)
            stats = self.get_file_stats(file_path)
            
            if stats:
                summary['files'][filename] = stats
            else:
                summary['files'][filename] = {'status': 'not_found'}
        
        return summary
    
    def safe_write_json(self, data, file_path):
        """Safely write JSON data to file with backup"""
        try:
            # Create backup if file exists
            if os.path.exists(file_path):
                backup_path = f"{file_path}.backup"
                shutil.copy2(file_path, backup_path)
            
            # Write new data
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            
            # Remove backup if write was successful
            backup_path = f"{file_path}.backup"
            if os.path.exists(backup_path):
                os.remove(backup_path)
            
            return True
            
        except Exception as e:
            # Restore backup if write failed
            backup_path = f"{file_path}.backup"
            if os.path.exists(backup_path):
                shutil.copy2(backup_path, file_path)
                os.remove(backup_path)
            
            raise Exception(f"Error writing JSON file: {str(e)}")
    
    def get_data_health_report(self):
        """Generate a health report for all data files"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'overall_status': 'healthy',
            'issues': [],
            'files': {}
        }
        
        # Check weather history
        history_file = os.path.join(self.data_folder, 'weather_history.txt')
        if os.path.exists(history_file):
            try:
                with open(history_file, 'r') as f:
                    lines = f.readlines()
                report['files']['weather_history.txt'] = {
                    'status': 'ok',
                    'record_count': len(lines)
                }
            except Exception as e:
                report['files']['weather_history.txt'] = {'status': 'error', 'error': str(e)}
                report['issues'].append(f"Weather history file error: {str(e)}")
        else:
            report['files']['weather_history.txt'] = {'status': 'missing'}
        
        # Check journal entries
        journal_file = os.path.join(self.data_folder, 'journal_entries.json')
        if os.path.exists(journal_file):
            valid, message = self.validate_json_file(journal_file)
            if valid:
                try:
                    with open(journal_file, 'r') as f:
                        data = json.load(f)
                    report['files']['journal_entries.json'] = {
                        'status': 'ok',
                        'entry_count': len(data) if isinstance(data, list) else 'unknown'
                    }
                except Exception as e:
                    report['files']['journal_entries.json'] = {'status': 'error', 'error': str(e)}
                    report['issues'].append(f"Journal file error: {str(e)}")
            else:
                report['files']['journal_entries.json'] = {'status': 'invalid', 'error': message}
                report['issues'].append(f"Journal file invalid: {message}")
        else:
            report['files']['journal_entries.json'] = {'status': 'missing'}
        
        # Set overall status
        if report['issues']:
            report['overall_status'] = 'has_issues'
        
        return report
