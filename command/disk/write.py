import command.command as command


class WriteCommand(command.Command):
    def __init__(self, write_target, block_size_kb, count_k):
        self.command = "dd if=/dev/zero of={} oflag=direct bs={}k count={}k".format(  # noqa E501
            write_target, block_size_kb, count_k
        )
        self.write_target = write_target
        self.block_size_kb = block_size_kb
        self.count_k = count_k

    def get_output_data(self):
        return {
            "speed": self.stderr.decode('utf-8').split("\n")[2].split(', ')[-1],  # noqa E501
            "write_target": self.write_target,
            "block_size (kb)": self.block_size_kb,
            "count (k)": self.count_k
        }
