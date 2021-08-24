#!/usr/bin/env python3

import connection.ssh as ssh_connection
import connection.local as local_connection
import config.connection as connection_config
import command.command as command
import argparse
import sys


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
        conn = ssh_connection.SSHConnection(
            connection_config.SSHConnectionConfiguration(
                args.username,
                args.password,
                args.address
            )
        )
    conn.connect()
    cmd = command.Command("whoami")
    conn.run_command(cmd)
    conn.close()
    sys.stderr.write(cmd.stderr.decode('utf-8'))
    sys.stdout.write(cmd.stdout.decode('utf-8'))


def get_configuration():
    parser = argparse.ArgumentParser("Perform a health check on a remote server")
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
