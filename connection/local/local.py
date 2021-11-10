import connection.connection as connection
import error.command as command_error
import shutil
import subprocess


class LocalConnection(connection.Connection):

    def __init__(self, configuration):
        super().__init__(configuration)

    def connect(self):
        pass

    def close(self):
        pass

    def run_command(self, command):
        cmd_arr = command.to_array()
        path_to_cmd = shutil.which(cmd_arr[0])
        if not path_to_cmd:
            raise command_error.CommandNotFoundError
        process = subprocess.Popen(
            cmd_arr,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if command.stdin:
            process.stdin.write(command.stdin.encode('utf-8'))
            process.stdin.close()
        process.wait()
        command.return_code = process.returncode
        command.stdout = process.stdout.read()
        command.stderr = process.stderr.read()

    def get_runtime_meta(self):
        return {
            "type": "local"
        }
