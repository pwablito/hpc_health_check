import check.check
import command.disk.read as read_command


class ReadCheck(check.check.Check):
    def run(self):
        command = read_command.ReadCommand(
            self.configuration.read_target,
            self.configuration.block_size_kb,
            self.configuration.count_k,
        )
        self.connection.run_command(command)
        read_data = command.get_output_data()
        self.result = read_data
