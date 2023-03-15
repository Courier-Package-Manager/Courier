"""
Courier.util.setup
~~~~~~~~~~~~~~~~~~~~

This module contains utility function(s) that
are used for formatting and general aethetics.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

import datetime
import re

from .update import load_logging_ini
import logging
import colorama

load_logging_ini()
logger = logging.getLogger()


def get_date(
    date: datetime.datetime, day=datetime.datetime.now().strftime("%d")
) -> str:
    """Return a colorized version of timestamp

    :param date: timestamp as a `datetime.datetime` instance
    :param day: (optional) String of current day without x0 format

    :return: Formatted string of the current date
    :rtype: string
    """

    match int(day):
        case 1:
            postfix = "st"
        case 2:
            postfix = "nd"
        case 3:
            postfix = "rd"
        case _:
            postfix = "th"

    day = colorama.Fore.MAGENTA + day + postfix + "," + colorama.Fore.RESET
    month = colorama.Fore.BLUE + date.strftime("%B") + colorama.Fore.RESET
    year = colorama.Fore.BLUE + date.strftime("%Y") + colorama.Fore.RESET
    _date = f"{month} {day} {year}"

    return _date


def escape_ansi(line) -> str:
    """Remove formatting from colored string

    credit: Édouard Lopez

    :param line: Colored string with escape characters
    :return: string with escape characters removed
    :rtype: string
    """

    try:
        ansi_escape = re.compile(r"(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]")
        return ansi_escape.sub("", line)
    except Exception as raw_exception:
        logger.error(str(raw_exception))
        return line
