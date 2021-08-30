class WriteCheckConfiguration:

    working_dir = "/tmp"

    def __init__(self, block_size_kb, size_mb, iodepth, time_sec):
        self.block_size_kb = block_size_kb
        self.size_mb = size_mb
        self.iodepth = iodepth
        self.time_sec = time_sec
