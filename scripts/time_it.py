#!/usr/bin/env python3
"""
Measure execution time of program
"""
from os.path import basename
import subprocess
from timeit import default_timer as now
from datetime import timedelta

def main(args):
    """
    Parse arguments and execute script
    """
    script_name = basename(args.pop(0))

    if len(args) > 0:
        command = str.join(' ', args)
        print('Running: ', command)
    else:
        print('USAGE: ', script_name, ' command')
        sys.exit(1)

    start = now()
    subprocess.call(command, shell=True)
    print(timedelta(seconds=now()-start))

if __name__ == '__main__':
    import sys
    main(sys.argv)
