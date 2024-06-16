import subprocess
import json
import yaml
import logging
import os

class ConfigManager:
    def __init__(self, static_config_path='static-config.json'):
        self.static_config_path = static_config_path

    def load_yaml(self, file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def load_json(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def save_json(self, data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def read_backup(self, backup_file_path):
        binary_path = os.path.join(os.path.dirname(__file__), '..', 'bin', 'decode-config')
        try:
            # Call the decode-config binary
            result = subprocess.run(
                [binary_path, '--source', backup_file_path, '--output-format', 'json'],
                capture_output=True,
                text=True,
                check=True
            )
            backup_data = json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to decode backup file: {e}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse JSON from decoded data: {e}")
            raise

        # Save the entire backup data to new-static-config.json
        self.save_json(backup_data, 'new-static-config.json')

        # Extract custom configuration keys
        custom_keys = [
            'ip_address', 'devicename', 'friendlyname', 'ota_url', 
            'mqtt_user', 'mqtt_pwd', 'mqtt_host', 'mqtt_port', 
            'sta_config', 'sta_ssid', 'sta_pwd', 'wifi_bssid', 
            'wifi_channel', 'templatename'
        ]
        new_custom_config = {key: backup_data[key] for key in custom_keys if key in backup_data}
        self.save_json(new_custom_config, 'new-custom-config.json')

        # Generate updated-static-config.json by comparing with static-config.json
        static_config = self.load_json(self.static_config_path)
        updated_static_config = {k: v for k, v in backup_data.items() if k not in static_config or static_config[k] != v}
        self.save_json(updated_static_config, 'updated-static-config.json')

        logging.info("Generated new-static-config.json, new-custom-config.json, and updated-static-config.json")

    def merge_configs(self):
        static_config = self.load_json(self.static_config_path)
        updated_static_config = self.load_json('updated-static-config.json')
        new_custom_config = self.load_json('new-custom-config.json')

        # Merge updated-static-config.json into static-config.json
        merged_config = static_config.copy()
        merged_config.update(updated_static_config)

        # Merge new-custom-config.json into the merged_config
        merged_config.update(new_custom_config)

        self.save_json(merged_config, 'final-merged-config.json')
        logging.info("Generated final-merged-config.json")

