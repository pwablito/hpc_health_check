import connection.ssh.ssh as ssh_connection
import error.ssh as ssh_error
import paramiko
import util.totp as totp_util


class SSHTOTPConnection(ssh_connection.SSHConnection):
    def connect(self):
        def handler(_, __, fields):
            if len(fields) != 2:
                raise ssh_error.InvalidAuthException
            return [
                self.configuration.password,
                totp_util.get_totp_code(self.configuration.totp_seed)
            ]
        transport = paramiko.Transport(
            (self.configuration.address, self.configuration.port)
        )
        transport.connect(username=self.configuration.username)
        transport.auth_interactive(self.configuration.username, handler)
        self.client = paramiko.SSHClient()
        # PR #1899 in https://github.com/paramiko/paramiko makes this easier
        self.client._transport = transport
