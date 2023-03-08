"""
The MIT License (MIT)

Copyright (c) 2023 Joshua Rose

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

Description: Extra utility functions that are used for formatting
"""

import datetime
import colorama


def get_date(_date, day=datetime.datetime.now().strftime('%-d')) -> str:
    """
    Return a 🎆 colorized 🎆 version of timestamp
    ts: timestamp (Datetime object)

    return: string
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
    month = colorama.Fore.BLUE + _date.strftime("%B") + colorama.Fore.RESET
    year = colorama.Fore.BLUE + _date.strftime("%Y") + colorama.Fore.RESET
    date = f"{month} {day} {year}"

    return date
