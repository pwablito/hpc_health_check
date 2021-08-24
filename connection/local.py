import connection.connection as connection
import subprocess


class LocalConnection(connection.Connection):

    def __init__(self, configuration):
        super().__init__(configuration)

    def connect(self):
        pass

    def close(self):
        pass

    def run_command(self, command):
        proc = subprocess.run(command.to_array(), capture_output=True, stdin=command.stdin)
        command.stderr = proc.stderr
        command.stdout = proc.stdout
