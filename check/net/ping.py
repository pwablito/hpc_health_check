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
            time = 0  # TODO run a ping command and get the time
            for line in output.split():
                if "time=" in line:
                    time = float(line.split("=")[1])
            assert time
            times.append(time)
        self.result = {
            "ping": {
                "times": times,
                "average": math_util.mean(times)
            }
        }
