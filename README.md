# Tasmonator

This tool is designed to configure Tasmota devices using static and custom configuration files, and to generate these configurations from a Tasmota backup. The project is structured to allow easy extension and maintenance.

## Features

- Configure Tasmota devices with static and custom configurations.
- Generate YAML configuration files from a Tasmota backup.
- Log Tasmota device console output and tool actions for easy debugging.

## Installation

### Prerequisites

- Python 3.6 or higher
- `pip` package installer

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/michaelkandziora/tasmota.configuration-tool.git
    cd tasmota.configuration-tool
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the package:

    ```bash
    pip install -e .
    ```

## Usage

### Configure a Tasmota Device

To configure a Tasmota device, you need its IP address and optionally a custom configuration YAML file.

```bash
tasmonator configure <ip_address> <path_to_custom_config.yaml> --debug
```

- `ip_address`: The IP address of the Tasmota device.
- `path_to_custom_config.yaml`: (Optional) Path to the custom configuration YAML file.
- `--debug`: (Optional) Enable debug mode for detailed logging.

Example:

```bash
tasmonator configure 192.168.0.100 ./custom-config.yaml --debug
```

### Read a Tasmota Backup

To generate YAML configuration files from a Tasmota backup, you need the path to the backup file.

```bash
tasmonator readbackup <path_to_backup_file>
```

Example:

```bash
tasmonator readbackup /path/to/Config_tasmota_C84A60_2656_13.4.0.dmp
```

This will generate `new-static-config.yaml` and `new-custom-config.yaml` in the current directory.

## Project Structure

```
tasmonator/
│
├── tasmonator/
│   ├── __init__.py
│   ├── cli.py
│   ├── config_manager.py
│   ├── device_manager.py
│   ├── exceptions.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   ├── test_config_manager.py
│   ├── test_device_manager.py
│   └── test_utils.py
│
├── static-config.yaml
├── custom-config.yaml
├── Config_tasmota_C84A60_2656_13.4.0.dmp
└── setup.py
```

### `tasmonator` Module

- `cli.py`: Command-line interface for the tool.
- `config_manager.py`: Manages configuration file operations.
- `device_manager.py`: Manages communication and configuration of Tasmota devices.
- `exceptions.py`: Custom exception classes.
- `utils.py`: Utility functions.

### Tests

Unit tests are located in the `tests/` directory. To run the tests, use:

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the existing coding standards and includes appropriate test coverage.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.