#!/usr/bin/env python3
"""
Convert UNIX epoch to a ISO date and vice versa.
"""

import calendar
import datetime
import re
import time


VALID_EPOCH = re.compile(r'^\d+$')
VALID_DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
VALID_TIME = re.compile(r'^\d{2}:\d{2}:\d{2}$')
DATE_TIME_FMT = "%Y-%m-%d %H:%M:%S"
DEFAULT_TIME = '00:00:00'


def unix_epoch_to_date(unix_epoch):
    """Converts a UNIX epoch to a date string."""

    return datetime.datetime.utcfromtimestamp(unix_epoch) \
                            .replace(tzinfo=datetime.timezone.utc) \
                            .strftime(DATE_TIME_FMT)


def date_time_to_unix_epoch(date_time):
    """Converts a date string to a UNIX epoch."""

    return calendar.timegm(time.strptime(date_time, DATE_TIME_FMT))


if __name__ == '__main__':
    import sys
    from os.path import basename

    CONVERT_FROM_EPOCH = None

    if len(sys.argv) in (2, 3):
        if len(sys.argv) == 2 and VALID_EPOCH.match(sys.argv[1]):
            CONVERT_FROM_EPOCH = True
        if VALID_DATE.match(sys.argv[1]) and (len(sys.argv) == 2 or VALID_TIME.match(sys.argv[2])):
            if len(sys.argv) == 2:
                sys.argv.append(DEFAULT_TIME)
            CONVERT_FROM_EPOCH = False

    if CONVERT_FROM_EPOCH is None:
        SCRIPT_NAME = basename(sys.argv[0])
        print("Usage:")
        print(f"  {SCRIPT_NAME} <unix_epoch> -- Convert UNIX epoch to ISO date")
        print(f"  {SCRIPT_NAME} <date> [<time>] -- Convert ISO date to UNIX epoch")
        sys.exit(1)

    print(unix_epoch_to_date(int(sys.argv[1])) if CONVERT_FROM_EPOCH
          else date_time_to_unix_epoch(' '.join(sys.argv[1:])))
