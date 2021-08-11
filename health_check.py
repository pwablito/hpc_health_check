#!/usr/bin/env python3

import argparse


def main():
    get_configuration()


def get_configuration():
    parser = argparse.ArgumentParser(description='Perform a health check on a remote server')
    return parser.parse_args()


if __name__ == "__main__":
    main()
