# Tasmonator

Tasmonator is a tool for configuring Tasmota devices and managing their configuration backups.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/michaelkandziora/tasmota.configuration-tool
    cd tasmota.configuration-tool
    ```

2. **Setup the virtual environment and install dependencies**:

    ```bash
    make
    ```

## Usage

### Read Backup File

This command reads a Tasmota backup file and generates `new-static-config.json`, `new-custom-config.json`, and `updated-static-config.json`.

```bash
tasmonator readbackup ./Config_tasmota_C84A60_2656_13.4.0.dmp
```

### Merge Configurations

This command merges `static-config.json`, `updated-static-config.json`, and `new-custom-config.json` into `final-merged-config.json`.

```bash
tasmonator mergeconfigs
```

### Configure Device

This command configures a Tasmota device using the provided custom configuration.

```bash
tasmonator configure <ip_address> <custom_config.json> --debug
```

### Example

```bash
tasmonator configure 192.168.0.100 new-custom-config.json --debug
```

## Contributing

Feel free to submit issues and pull requests to contribute to the project.

## License

This project is licensed under the MIT License.