#!/usr/bin/env python3

import connection.ssh as ssh_connection
import config.connection as connection_config
import command.command as command
import argparse
import sys


def main():
    args = get_configuration()
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
    sys.stderr.write(cmd.stderr.decode())
    sys.stdout.write(cmd.stdout.decode())
    conn.close()


def get_configuration():
    parser = argparse.ArgumentParser(description='Perform a health check on a remote server')
    parser.add_argument('--address', help='The address of the remote server')
    parser.add_argument('--username', help='The username to use when authenticating with the remote server')
    parser.add_argument('--password', help='The password to use when authenticating with the remote server')
    return parser.parse_args()


if __name__ == "__main__":
    main()
