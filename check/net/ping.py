import check.check as check
import util.math as math_util
import command.net.ping as ping_command


class PingCheck(check.Check):
    def run(self):
        times = []
        for i in range(self.configuration.ping_tests):
            command = ping_command.PingCommand(self.configuration.ping_address)
            self.connection.run_command(command)
            output = command.stdout.decode('utf-8')
            # TODO this is a very hacky way to parse the ping output
            time = None
            for line in output.split():
                if "time=" in line:
                    time = float(line.split("=")[1])
            # Make sure the time output was captured and time is not still 0
            assert time is not None
            times.append(time)
        self.result = {
            "ping": {
                "samples": times,
                "average": math_util.mean(times),
                "target": self.configuration.ping_address
            }
        }
