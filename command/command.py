class Command:

    stdin = None
    stdout = None
    stderr = None

    def __init__(self, command):
        self.command = command

    def to_array(self):
        # TODO implement more parsing (quotes, etc)
        return self.command.split()

    def get_output_data(self):
        raise NotImplementedError
