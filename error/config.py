class ConfigurationException(Exception):
    pass


class MissingConfigurationException(ConfigurationException):
    pass


class InvalidConfigurationException(ConfigurationException):
    pass


class UnsupportedConfigurationTypeException(ConfigurationException):
    pass
