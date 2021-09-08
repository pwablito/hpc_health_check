import unittest
import config.file
import check.disk.read


class ConfigFileTestCase(unittest.TestCase):
    def test_validate(self):
        config_dict = {
            "connections": [],
            "checks": [
                {
                    "name": "test",
                    "check": check.disk.read.ReadCheck,
                }
            ]
        }
        config.file.validate_config_dict(config_dict, config.file.valid_config)
