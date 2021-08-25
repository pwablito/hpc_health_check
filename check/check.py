class Check:
    def __init__(self, configuration, connection):
        self.configuration = configuration
        self.result = None
        self.connection = connection

    def run(self):
        raise NotImplementedError
