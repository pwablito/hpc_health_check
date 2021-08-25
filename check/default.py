import check.gpu.nvidia as nvidia_check
import config.check.gpu.nvidia as nvidia_check_config
import check.net.ping as ping_check
import config.check.net.ping as ping_check_config


def get_default_checks():
    return {
        'nvidia': {
            "check": nvidia_check.NvidiaCheck,
            "config": nvidia_check_config.NvidiaCheckConfiguration()
        },
        'ping': {
            "check": ping_check.PingCheck,
            "config": ping_check_config.PingCheckConfiguration(50, "google.com")
        }
    }
