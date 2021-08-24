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
        process = subprocess.Popen(
            command.to_array(),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if command.stdin:
            process.stdin.write(command.stdin.encode('utf-8'))
            process.stdin.close()
        process.wait()
        command.stdout = process.stdout.read()
        command.stderr = process.stderr.read()
