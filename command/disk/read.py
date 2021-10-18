import command.command as command


class ReadCommand(command.Command):
    def __init__(self, read_target, block_size_kb, count_k):
        self.command = "dd if={} of=/dev/null bs={}k count={}k".format(  # noqa E501
            read_target, block_size_kb, count_k
        )
        self.read_target = read_target
        self.block_size_kb = block_size_kb
        self.count_k = count_k

    def get_output_data(self):
        return {
            "speed": self.stderr.decode('utf-8').split("\n")[2].split(', ')[-1],  # noqa E501
            "read_target": self.read_target,
            "block_size (kb)": self.block_size_kb,
            "count (k)": self.count_k
        }
