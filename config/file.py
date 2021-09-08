import check
import config.check.check
import config.connection
import connection.connection
import json
import logging


valid_config = {
    "connections": [
        {
            "type": connection.connection.Connection,
            "config": config.connection.connection.ConnectionConfiguration
        }
    ],
    "checks": [
        {
            "name": str,
            "check": check.Check,
            "config": config.check.check.CheckConfiguration
        }
    ]
}


def get_config_dict(path):
    try:
        return json.load(open(path))
    except FileNotFoundError:
        logging.error('File not found: {}'.format(path))
        exit(1)


def validate_config_list(config_list, valid_config_list):
    pass


def validate_config_dict(config_dict, valid_config_dict):
    logging.info('Validating configuration')
    for key in config_dict.items():
        if key not in valid_config_dict:
            raise Exception('Invalid configuration key: {}'.format(key))
        valid_type = valid_config_dict[key]
        if not isinstance(valid_type, type):
            valid_type = type(valid_type)
        if not isinstance(config_dict[key], valid_type):
            raise Exception('Invalid configuration value: {}'.format(key))
        if valid_type == list:
            validate_config_list(config_dict[key], valid_config_dict[key])
        if valid_type == dict:
            validate_config_dict(config_dict[key], valid_config_dict[key])


def get_config(config_file_path):
    config_dict = get_config_dict(config_file_path)
    logging.info('Config file contents: {}'.format(json.dumps(config_dict)))
    validate_config_dict(config_dict, valid_config)
