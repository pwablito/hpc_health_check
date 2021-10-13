import check.check as check
import command.disk.write as write_command


class WriteCheck(check.Check):
    def run(self):
        command = write_command.WriteCommand(
            self.configuration.block_size_kb,
            self.configuration.size_mb,
            self.configuration.iodepth,
            self.configuration.time_sec
        )
        self.connection.run_command(command)
        write_data = command.get_output_data()
        self.result = write_data
