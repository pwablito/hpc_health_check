class SSHConnectionConfiguration:
    def __init__(self, username, password, address, port=22):
        self.username = username
        self.password = password
        self.address = address
        self.port = port