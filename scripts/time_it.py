#!/usr/bin/env python3
"""
Run a program and then print the number seconds the program ran.
"""

import subprocess

from datetime import timedelta
from timeit import default_timer as now


def time_it(program_and_args, verbose=False):
    """Returns the time (in seconds) it takes to run a program."""

    if len(program_and_args) == 0:
        raise ValueError('program_and_args must contain at least one element')

    program = str.join(' ', program_and_args)

    if verbose:
        print(f"Running: {program}")

    start_time = now()

    subprocess.call(program, shell=True)

    return timedelta(seconds=now()-start_time).total_seconds()


if __name__ == '__main__':
    import sys
    from os.path import basename

    if len(sys.argv) == 1:
        print(f"USAGE: {basename(sys.argv[0])} program [program args...]")
        sys.exit(1)

    print(f'Elapsed: {time_it(sys.argv[1:], verbose=True):.2f} s')
