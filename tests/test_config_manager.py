import unittest
from tasmonator.config_manager import ConfigManager

class TestConfigManager(unittest.TestCase):

    def setUp(self):
        self.config_manager = ConfigManager()

    def test_load_yaml(self):
        data = self.config_manager.load_yaml('tests/test_static_config.yaml')
        self.assertIsInstance(data, dict)

    def test_read_backup(self):
        self.config_manager.read_backup('tests/test_backup.dmp')
        # Add assertions to validate the output

if __name__ == '__main__':
    unittest.main()
