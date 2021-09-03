import check.gpu.nvidia as nvidia_check
import config.check.gpu.nvidia as nvidia_check_config
import check.net.ping as ping_check
import config.check.net.ping as ping_check_config
import check.disk.read as read_check
import config.check.disk.read as read_check_config
import check.disk.write as write_check
import config.check.disk.write as write_check_config


def get_default_checks():
    return [
        {
            "name": "nvidia",
            "check": nvidia_check.NvidiaCheck,
            "config": nvidia_check_config.NvidiaCheckConfiguration()
        },
        {
            "name": "ping",
            "check": ping_check.PingCheck,
            "config": ping_check_config.PingCheckConfiguration(5, "google.com")
        },
        {
            "name": "disk_read",
            "check": read_check.ReadCheck,
            "config": read_check_config.ReadCheckConfiguration(16, 256, 16, 5)
        },
        {
            "name": "disk_write",
            "check": write_check.WriteCheck,
            "config": write_check_config.WriteCheckConfiguration(16, 256, 16, 5)
        }
    ]
