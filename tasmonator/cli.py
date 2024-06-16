import argparse
import logging
from tasmonator.config_manager import ConfigManager
from tasmonator.device_manager import DeviceManagers

def configure_device(ip_address, custom_config_path=None, debug=False):
    config_manager = ConfigManager()
    static_config = config_manager.load_yaml('static-config.yaml')
    custom_config = config_manager.load_yaml(custom_config_path) if custom_config_path else {}

    logging.basicConfig(filename=f'{ip_address}.log', level=logging.DEBUG if debug else logging.INFO)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG if debug else logging.INFO)
    logging.getLogger().addHandler(console)

    device_manager = DeviceManager(ip_address)
    device_manager.configure_device(static_config, custom_config)

def read_backup(backup_file_path):
    config_manager = ConfigManager()
    config_manager.read_backup(backup_file_path)

def main():
    parser = argparse.ArgumentParser(description="Tasmota Device Configuration Tool")
    subparsers = parser.add_subparsers(dest='command')

    configure_parser = subparsers.add_parser('configure', help='Configure a Tasmota device')
    configure_parser.add_argument('ip_address', help='IP address of the Tasmota device')
    configure_parser.add_argument('custom_config', nargs='?', help='Path to the custom configuration YAML file')
    configure_parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    backup_parser = subparsers.add_parser('readbackup', help='Read Tasmota backup and generate YAML files')
    backup_parser.add_argument('backup_file_path', help='Path to the Tasmota backup file')

    args = parser.parse_args()
    if args.command == 'configure':
        configure_device(args.ip_address, args.custom_config, args.debug)
    elif args.command == 'readbackup':
        read_backup(args.backup_file_path)

if __name__ == "__main__":
    main()
