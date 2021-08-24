import connection.connection as connection
import error.ssh as ssh_error
import error.command as command_error
import paramiko


class SSHConnection(connection.Connection):

    def __init__(self, configuration):
        super().__init__(configuration)
        self.client = None

    def assert_client_connected(self):
        if not self.client:
            raise ssh_error.NotConnectedError

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            self.configuration.address,
            self.configuration.port,
            self.configuration.username,
            self.configuration.password
        )

    def close(self):
        self.assert_client_connected()
        self.client.close()

    def run_command(self, command):
        try:
            self.assert_client_connected()
            stdin, stdout, stderr = self.client.exec_command(command.command)
            if command.stdin:
                stdin.channel.send(command.stdin)
                stdin.channel.shutdown_write()
            command.stdout = stdout.read()
            command.stderr = stderr.read()
        except FileNotFoundError:
            raise command_error.CommandNotFoundError
