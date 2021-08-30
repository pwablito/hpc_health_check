import command.command as command


class ReadCommand(command.Command):
    def __init__(self, block_size_kb, size_mb, iodepth, time_sec):
        # TODO set cwd before running
        self.command = "fio --name=random-read --ioengine=posixaio --rw=randread --bs={}k --size={}m --numjobs=1 --iodepth={} --runtime={} --time_based --end_fsync=1".format(  # noqa
            block_size_kb, size_mb, iodepth, time_sec
        )

    def get_output_data(self):
        raise NotImplementedError
