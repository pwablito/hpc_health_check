import check.check as check
import math


class PingCheck(check.Check):
    def run(self):
        times = []
        for i in range(self.configuration.ping_tests):
            time = 0  # TODO run a ping command and get the time
            times.append(time)
        self.result = {
            "ping": {
                "times": times,
                "average": math.mean(times)
            }
        }
