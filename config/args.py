import check.default as default_check
import argparse


def get_configuration():
    parser = argparse.ArgumentParser(
        "Perform a health check"
    )
    subparsers = parser.add_subparsers(dest='command', required=True)
    subparsers.add_parser("test")
    file_parser = subparsers.add_parser("file")
    file_parser.add_argument("filename", type=str)
    local_parser = subparsers.add_parser("local")
    add_check_arg(local_parser)
    ssh_parser = subparsers.add_parser("ssh")
    add_check_arg(ssh_parser)
    ssh_parser.add_argument(
        '--address',
        help='The address of the remote server',
        required=True
    )
    ssh_parser.add_argument(
        '--username',
        help='The username to use when authenticating with the remote server',
        required=True
    )
    ssh_parser.add_argument(
        '--password',
        help='The password to use when authenticating with the remote server',
        required=False  # Not always needed, so not required
    )
    return parser.parse_args()


def add_check_arg(parser):
    parser.add_argument(
        '--check',
        nargs='+',
        choices=['all'] + [
            check_dict["name"]
            for check_dict in default_check.get_default_checks()
        ],
        default='all'
    )
