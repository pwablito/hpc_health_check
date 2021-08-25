#!/usr/bin/env python3

import connection.ssh.ssh as ssh_connection
import connection.ssh.totp.totp as ssh_totp_connection
import connection.local.local as local_connection
import config.connection as connection_config
import check.default as default_check
import argparse
import json


def main():
    args = get_configuration()
    conn = None
    if args.command == "local":
        conn = local_connection.LocalConnection(
            connection_config.LocalConnectionConfiguration(
                args.username,
                args.password
            )
        )
    elif args.command == "ssh":
        config = connection_config.SSHConnectionConfiguration(
            args.username,
            args.password,
            args.address
        )
        if args.port:
            config.port = args.port
        if args.totp_seed:
            config.totp_seed = args.totp_seed
        if args.totp_seed:
            conn = ssh_totp_connection.SSHTotpConnection(config)
        else:
            conn = ssh_connection.SSHConnection(config)
    conn.connect()

    checks_to_run = []
    all_args = "all" in args.check
    for check_name, check_dict in default_check.get_default_checks().items():
        if all_args or check_name in args.check:
            checks_to_run.append(check_dict)
    check_results = []
    for check in checks_to_run:
        check_inst = check["check"](check["config"], conn)
        check_inst.run()
        check_results.append(check_inst.result)
    if len(check_results):
        print(json.dumps(check_results))


def get_configuration():
    parser = argparse.ArgumentParser(
        "Perform a health check"
    )
    parser.add_argument(
        '--check',
        nargs='+',
        choices=['all'] + [key for key in default_check.get_default_checks().keys()],
        default='all'
    )
    subparsers = parser.add_subparsers(dest='command', required=True)
    local_parser = subparsers.add_parser("local")
    local_parser.add_argument(
        "--username",
        help="The user to run commands as",
        required=True
    )
    local_parser.add_argument(
        '--password',
        help='The password for provided user',
        required=False  # Not always needed, so not required
    )
    ssh_parser = subparsers.add_parser("ssh")
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


if __name__ == "__main__":
    main()
