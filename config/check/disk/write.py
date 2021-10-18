import config.check.check


class WriteCheckConfiguration(config.check.check.CheckConfiguration):
    working_dir = "/tmp"

    def __init__(self, write_target, block_size_kb, count_k):
        self.write_target = write_target
        self.block_size_kb = block_size_kb
        self.count_k = count_k
