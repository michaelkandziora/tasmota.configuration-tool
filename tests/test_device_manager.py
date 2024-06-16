import unittest
from unittest.mock import patch
from tasmonator.device_manager import DeviceManager

class TestDeviceManager(unittest.TestCase):

    def setUp(self):
        self.device_manager = DeviceManager('192.168.0.100')

    @patch('tasmonator.device_manager.requests.get')
    def test_send_tasmota_command(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'OK'
        response = self.device_manager.send_tasmota_command('TestCommand')
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
