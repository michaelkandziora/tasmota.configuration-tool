import unittest
from tasmonator.utils import load_yaml

class TestUtils(unittest.TestCase):

    def test_load_yaml(self):
        data = load_yaml('tests/test_static_config.yaml')
        self.assertIsInstance(data, dict)

if __name__ == '__main__':
    unittest.main()
