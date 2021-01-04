#!/usr/bin/env python3
"""
Print environment variables
"""
import os


def print_variable(name, value):
    """Prints the variable's name and value unless the value is undefined."""

    if value:
        print(f"{name}={value}")


def print_all_env_vars():
    """Prints all environment variables."""

    for item in os.environ.items():
        print_variable(item[0], item[1])


def print_env_vars(names):
    """Prints the environment variables listed in names."""

    for name in names:
        print_variable(name, os.getenv(name))


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        print_all_env_vars()
    else:
        print_env_vars(sys.argv[1:])
