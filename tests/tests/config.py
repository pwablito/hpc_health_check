import unittest
import config.file
import check.disk.read
import config.check.disk.read as read_check_config
import config.check.net.ping
import config.connection.connection
import config.parser
import error.config


class ConfigFileTestCase(unittest.TestCase):
    def test_validate_config(self):
        config.file.validate_config_dict({
            "connections": [{
                "type": "connection.local.local.LocalConnection",
                "config": "config.connection.connection.LocalConnectionConfiguration()"
            }],
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
                "connections": [{
                    "type": "connection.local.local.LocalConnection",
                    "config": "config.connection.connection.LocalConnectionConfiguration()"
                }],
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
                "connections": [{
                    "type": "connection.local.local.LocalConnection",
                    "config": "config.connection.connection.LocalConnectionConfiguration()"
                }],
                "checks": [
                    {
                        "name": "test",
                        "check": check.disk.read.ReadCheck
                    }
                ]
            }, config.file.valid_config)
        with self.assertRaises(error.config.InvalidConfigurationException):
            config.file.validate_config_dict({
                "connections": [{
                    "type": "connection.local.local.LocalConnection",
                    "config": "config.connection.connection.LocalConnectionConfiguration()"
                }],
                "checks": [
                    {
                        "name": "test",
                        "check": check.disk.read.ReadCheck,
                        "config": "invalid_config_value"
                    }
                ]
            }, config.file.valid_config)


class ConfigParserTestCase(unittest.TestCase):
    def test_load_object_from_string(self):
        self.assertEqual(
            config.parser.load_object_from_string(
                'config.check.net.ping.PingCheckConfiguration'
            ),
            config.check.net.ping.PingCheckConfiguration
        )
        obj = config.check.net.ping.PingCheckConfiguration(1, "test")
        test_obj = config.parser.load_object_from_string(
            'config.check.net.ping.PingCheckConfiguration(1, "test")'
        )
        self.assertEqual(obj, test_obj)

    def test_load_config_from_string(self):
        raw_config = {
            "connections": [{
                "type": "connection.local.local.LocalConnection",
                "config": "config.connection.connection.LocalConnectionConfiguration()"
            }],
            "checks": [
                {
                    "name": "test",
                    "check": "check.disk.read.ReadCheck",
                    "config": "config.check.disk.read.ReadCheckConfiguration(16, 256, 16, 5)"
                }
            ]
        }
        typed_config = config.parser.expand_config_types(raw_config)
        assert(typed_config["checks"][0]["check"] == check.disk.read.ReadCheck)
        assert(type(typed_config["checks"][0]["config"]) == read_check_config.ReadCheckConfiguration)
        assert(type(typed_config["connections"][0]["config"]) == config.connection.connection.LocalConnectionConfiguration)
