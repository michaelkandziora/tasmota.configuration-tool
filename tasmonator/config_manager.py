import yaml
import json
import os
import logging

class ConfigManager:
    def __init__(self, static_config_path='static-config.yaml'):
        self.static_config_path = static_config_path

    def load_yaml(self, file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def read_backup(self, backup_file_path):
        with open(backup_file_path, 'r') as file:
            backup_data = json.load(file)

        new_static_config = {}
        new_custom_config = {}

        # Extract static config from backup
        static_keys = [
            'NAME', 'GPIO', 'FLAG', 'BASE', 'CMND', 
            'Module', 'HostName', 'IPAddress1', 'IPAddress2', 
            'IPAddress3', 'WebServer', 'Sleep', 'LedState'
        ]
        for key in static_keys:
            if key in backup_data:
                new_static_config[key.lower()] = backup_data[key]

        # Extract custom config from backup
        custom_keys = [
            'FriendlyName', 'Power', 'LedPower', 'RelayState', 
            'Temperature', 'Humidity', 'Dimmer', 'Color'
        ]
        for key in custom_keys:
            if key in backup_data:
                new_custom_config[key.lower()] = backup_data[key]

        with open('new-static-config.yaml', 'w') as file:
            yaml.dump(new_static_config, file)

        with open('new-custom-config.yaml', 'w') as file:
            yaml.dump(new_custom_config, file)

        logging.info("Generated new-static-config.yaml and new-custom-config.yaml")
