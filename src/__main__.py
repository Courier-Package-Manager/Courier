# -*- coding=utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2023 Joshua Rose

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
"""

import os
import json
import logging
from datetime import datetime

from posix import DirEntry
from logging.config import fileConfig

fileConfig('config.ini')
logger = logging.getLogger()

try:
    import colorama
except ImportError:
    logger.critical("Dependencies are not installed. run \'make install\' to install.")
    raise SystemExit

colorama.init()

PACKAGE = 'update.json'


def scan_dir(files=True, folders=True) -> list[DirEntry]:
    """ A better version of the os.scandir function, as it takes multiple args. """
    items = []
    for item in os.scandir(os.getcwd()):
        items.append(item)
    if not files:
        [items.remove(item) for item in items if os.path.isfile(item)]
    if not folders:
        [items.remove(item) for item in items if os.path.isdir(item)]
    return items


def loc_package_file():
    """
     - Locate the package file
     - Create package file if it doesn't exist.
    return: str
    """
    project_folder = os.path.basename(os.path.normpath(os.getcwd()))
    if project_folder != 'Courier': os.chdir('..')
    for file in scan_dir(files=True, folders=False):
        if file.name == PACKAGE:
            return file

    logger.info(" 📨 Creating {green}{package}{reset} in {magenta}{cwd}{reset}".format(
        green=colorama.Fore.GREEN,
        reset=colorama.Fore.RESET,
        magenta=colorama.Fore.MAGENTA,
        cwd=os.getcwd(),
        package=PACKAGE))

    with open(PACKAGE, 'w', True, 'UTF-8') as fp:
        ts = datetime.now().timestamp()
        data = {
                "created": ts,
                "dependencies": {}
                }
        json.dump(data, fp)
        fp.close()


def get_date(timestamp=datetime.now().timestamp) -> str:
    """ Return a 🎆 colorized 🎆 version of timestamp """

    ts = timestamp
    day = ts.strftime("%-d")

    match int(day):
        case 1: postfix = 'st'
        case 2: postfix = 'nd'
        case 3: postfix = 'rd'
        case _: postfix = 'th'

    date = "{blue}{month}{reset} {purple}{day}{postfix},{reset} {blue}{year}{reset}".format(
            purple=colorama.Fore.MAGENTA,
            blue=colorama.Fore.BLUE,

            reset=colorama.Fore.RESET,
            postfix=postfix,

            day=day,
            month=ts.strftime("%B"),
            year=ts.strftime("%Y"))

    return date


def last_updated():
    """ last update in datetime format. """
    # NOTE this is assuming that the following code has run:
    # >>> if project_folder != 'Courier': os.chdir('..') 
    data = json.load(open(PACKAGE, 'r'))
    timestamp = datetime.fromtimestamp(data['created'])
    date = get_date(timestamp=timestamp)
    return date



def update_packages():
    """ The core function of this entire repo """
    # TODO auto read python files and add dependencies
    ...

if __name__ == "__main__":
    loc_package_file()
    logger.debug("Package file {magenta}{package}{reset} was created {date}".format(
        magenta=colorama.Fore.GREEN,
        package=PACKAGE,
        reset=colorama.Fore.RESET,
        date=last_updated()))
