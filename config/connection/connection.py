class ConnectionConfiguration:
    pass


class SSHConnectionConfiguration(ConnectionConfiguration):
    def __init__(self, username, password, address):
        # TODO add support to TOTP seeds and custom ports
        self.username = username
        self.password = password
        self.address = address
        # TODO make this configurable
        self.port = 22


class LocalConnectionConfiguration(ConnectionConfiguration):
    # TODO add support for running as another user, etc
    pass
