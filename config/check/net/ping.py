import config.check.check


class PingCheckConfiguration(config.check.check.CheckConfiguration):
    def __init__(self, ping_tests, ping_address):
        self.ping_tests = ping_tests
        self.ping_address = ping_address
