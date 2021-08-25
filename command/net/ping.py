import command.command as command
import io
import csv


class PingCommand(command.Command):
    def __init__(self, ping_address):
        self.command = 'ping -c 1 {}'.format(ping_address)

    def get_output_data(self):
        return list(csv.DictReader(io.StringIO(self.stdout)))
