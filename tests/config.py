import unittest
import config.file


class ConfigFileTestCase(unittest.TestCase):
    def test_validate(self):
        config_dict = {
            "connections": [],
            "checks": [
                {}
            ]
        }
        config.file.validate_config_dict(config_dict, config.file.valid_config)
