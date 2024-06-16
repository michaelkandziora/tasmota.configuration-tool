import requests
import logging

class DeviceManager:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def send_tasmota_command(self, command):
        url = f'http://{self.ip_address}/cm?cmnd={command}'
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"Sent command '{command}' to {self.ip_address}: {response.text}")
            return response.json()
        else:
            logging.error(f"Failed to send command '{command}' to {self.ip_address}")
            return None

    def configure_device(self, static_config, custom_config):
        if 'template' in static_config:
            self.send_tasmota_command(f'Template {static_config["template"]}')
        
        if 'cmds' in static_config:
            for cmd in static_config['cmds']:
                self.send_tasmota_command(cmd)

        if 'cmds' in custom_config:
            for cmd in custom_config['cmds']:
                self.send_tasmota_command(cmd)

        if 'ipaddress' in custom_config:
            ip_address_config = custom_config['ipaddress']
            ip_cmd = f'IPAddress1 {ip_address_config[0]}'
            mask_cmd = f'IPAddress3 {ip_address_config[1]}'
            gateway_cmd = f'IPAddress2 {ip_address_config[2]}'
            dns_cmd = f'IPAddress4 {ip_address_config[3]}'
            self.send_tasmota_command(ip_cmd)
            self.send_tasmota_command(mask_cmd)
            self.send_tasmota_command(gateway_cmd)
            self.send_tasmota_command(dns_cmd)

        self.send_tasmota_command('savedata 1')
        self.send_tasmota_command('restart 1')
