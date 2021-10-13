import check.check as check
import command.gpu.nvidia as nvidia_command


class NvidiaCheck(check.Check):
    def run(self):
        gpu_data = []
        command = nvidia_command.NvidiaSMICommand()
        self.connection.run_command(command)
        gpu_data = command.get_output_data()
        # TODO make gpu_data more clear
        self.result = {
            "nvidia": {
                "gpus": gpu_data
            }
        }
