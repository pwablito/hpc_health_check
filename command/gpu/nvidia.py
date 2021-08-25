import command.command as command
import io
import csv


class NvidiaSMICommand(command.Command):
    def __init__(self):
        self.command = 'nvidia-smi --query-gpu=timestamp,name,pci.bus_id,driver_version,pstate,pcie.link.gen.max,pcie.link.gen.current,temperature.gpu,utilization.gpu,utilization.memory,memory.total,memory.free,memory.used --format=csv'  # noqa E501

    def get_output_data(self):
        return list(csv.DictReader(io.StringIO(self.stdout)))
