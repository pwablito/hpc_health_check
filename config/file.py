import check.check
import config.check.check
import config.connection
import connection.connection
import error.config
import json
import logging
import importlib
import re


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
            "check": check.check.Check,
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
    if len(valid_config_list):
        compare_item = valid_config_list[0]
        for item in config_list:
            validate_config_item(item, compare_item)


def validate_config_dict(config_dict, valid_config_dict):
    logging.info('Validating configuration')
    checked_keys = []
    for key in config_dict.keys():
        try:
            valid_key = valid_config_dict[key]
            validate_config_item(config_dict[key], valid_key)
            checked_keys.append(key)
        except KeyError:
            raise error.config.InvalidConfigurationException
    for key in valid_config_dict.keys():
        if key not in checked_keys:
            raise error.config.MissingConfigurationException


def validate_config_item(config_item, valid_config_item):
    if isinstance(config_item, type(valid_config_item)):
        pass
    elif not isinstance(config_item, valid_config_item):
        raise error.config.InvalidConfigurationException
    if type(valid_config_item) == list:
        validate_config_list(config_item, valid_config_item)
    if type(valid_config_item) == dict:
        validate_config_dict(config_item, valid_config_item)


def get_config(config_file_path):
    config_dict = get_config_dict(config_file_path)
    logging.info('Config file contents: {}'.format(json.dumps(config_dict)))
    validate_config_dict(config_dict, valid_config)


def get_class_from_string(input_string):
    try:
        module_path, class_name = input_string.rsplit('.', 1)
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except ValueError:
        raise ImportError


def get_arguments_from_string(input_string):
    match = re.match(r'.*\((\".*\")(,\w*(\".*\"))*\)', input_string)
    if match is not None:
        # TODO implement this- should pull both int and str args from string
        raise NotImplementedError
    return None


def load_object_from_string(input_str):
    # TODO Add validation that it is valid python syntax first
    class_type = get_class_from_string(input_str)
    args = get_arguments_from_string(input_str)
    if args is None:
        return class_type
    return class_type(*args)
