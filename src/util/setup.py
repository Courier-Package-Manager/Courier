"""
Courier.util.setup
~~~~~~~~~~~~~~~~~~~~

This module contains utility function(s) that
are used for formatting and general aethetics.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

import datetime

import colorama


def get_date(date: datetime.datetime, day=datetime.datetime.now().strftime('%-d')) -> str:
    """ Return a ❇️ colorized ❇️ version of timestamp

    :param date: timestamp as a `datetime.datetime` instance
    :param day: (optional) String of current day without x0 format

    :return: Formatted string of the current date
    :rtype: string
    """

    match int(day):
        case 1:
            postfix = 'st'
        case 2:
            postfix = 'nd'
        case 3:
            postfix = 'rd'
        case _:
            postfix = 'th'

    day = colorama.Fore.MAGENTA + day + postfix + ',' + colorama.Fore.RESET
    month = colorama.Fore.BLUE + date.strftime("%B") + colorama.Fore.RESET
    year = colorama.Fore.BLUE + date.strftime("%Y") + colorama.Fore.RESET
    _date = f"{month} {day} {year}"

    return _date
