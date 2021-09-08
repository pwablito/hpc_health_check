class ConnectionConfiguration:
    pass


class SSHConnectionConfiguration(ConnectionConfiguration):
    def __init__(self, username, password, address, port=22, totp_seed=None):
        self.username = username
        self.password = password
        self.address = address
        self.port = port
        self.totp_seed = totp_seed


class LocalConnectionConfiguration(ConnectionConfiguration):
    # TODO add support for running as another user, etc
    pass
