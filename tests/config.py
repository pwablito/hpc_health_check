import unittest
import config.file
import check.disk.read
import config.check.disk.read as read_check_config
import error.config


class ConfigFileTestCase(unittest.TestCase):
    def test_validate(self):
        config.file.validate_config_dict({
            "connections": [],
            "checks": [
                {
                    "name": "test",
                    "check": check.disk.read.ReadCheck,
                    "config": read_check_config.ReadCheckConfiguration(
                        16, 256, 16, 5
                    )
                }
            ]
        }, config.file.valid_config)
        with self.assertRaises(error.config.InvalidConfigurationException):
            config.file.validate_config_dict({
                "connections": [],
                "checks": [
                    {
                        "name": "test",
                        "check": check.disk.read.ReadCheck,
                        "invalid_key": "invalid"
                    }
                ]
            }, config.file.valid_config)
        with self.assertRaises(error.config.MissingConfigurationException):
            config.file.validate_config_dict({
                "connections": [],
                "checks": [
                    {
                        "name": "test",
                        "check": check.disk.read.ReadCheck
                    }
                ]
            }, config.file.valid_config)
        with self.assertRaises(error.config.InvalidConfigurationException):
            config.file.validate_config_dict({
                "connections": [],
                "checks": [
                    {
                        "name": "test",
                        "check": check.disk.read.ReadCheck,
                        "config": "invalid_config_value"
                    }
                ]
            }, config.file.valid_config)
