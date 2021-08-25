import check.gpu.nvidia as nvidia_check
import config.check as config_check


def get_default_checks():
    return {
        'nvidia': nvidia_check.NvidiaCheck(config_check.gpu.nvidia.NvidiaCheckConfig()),
    }
