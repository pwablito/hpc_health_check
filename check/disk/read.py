import command.disk.read as read_command
import check.check as check


class ReadCheck(check.Check):
    def run(self):
        command = read_command.ReadCommand(
            self.configuration.block_size_kb,
            self.configuration.size_mb,
            self.configuration.iodepth,
            self.configuration.time_sec
        )
        self.connection.run_command(command)
        read_data = command.get_output_data()
        self.result = read_data
