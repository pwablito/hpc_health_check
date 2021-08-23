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
        cmd = subprocess.Popen(command.to_array(), stdin=command.stdin, stdout=command.stdout, stderr=command.stderr)
        cmd.wait()
