class Connection:

    def __init__(self, configuration):
        self.configuration = configuration

    def connect(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def run_command(self, command):
        raise NotImplementedError
