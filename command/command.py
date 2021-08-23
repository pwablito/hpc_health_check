class Command:
    def __init__(self, command):
        self.command = command
        self.stdin = None
        self.stdout = None
        self.stderr = None

    def to_array(self):
        # TODO implement more parsing (quotes, etc)
        return self.command.split()
