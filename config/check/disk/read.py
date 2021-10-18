import config.check.check


class ReadCheckConfiguration(config.check.check.CheckConfiguration):

    working_dir = "/tmp"

    def __init__(self, read_target, block_size_kb, count_k):
        self.read_target = read_target
        self.block_size_kb = block_size_kb
        self.count_k = count_k
