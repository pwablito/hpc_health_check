class SSHConnectionConfiguration:
    def __init__(self, username, password, address, port=22, totp_seed=None):
        self.username = username
        self.password = password
        self.address = address
        self.port = port
        self.totp_seed = totp_seed


class LocalConnectionConfiguration:
    def __init__(self, username, password):
        self.username = username
        self.password = password
