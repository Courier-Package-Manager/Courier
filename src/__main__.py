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

from posix import DirEntry
from logging.config import fileConfig
from datetime import datetime

fileConfig('config.ini')
logger = logging.getLogger()

try:
    import requests
    import colorama
except ImportError as exception:
    logger.critical("Dependencies are not installed. run \'make install\' to install.")
    raise SystemExit

colorama.init()

PACKAGE = 'update.json'


def scan_dir(files=True, folders=True) -> list[DirEntry]:
    """ A better version of the os.scandir function, as it takes multiple args. """
    items = []
    for item in os.scandir(os.getcwd()): items.append(item)
    if not files: [items.remove(item) for item in items if os.path.isfile(item)]
    if not folders: [items.remove(item) for item in items if os.path.isdir(item)]
    return items

def loc_package_file():
    """Locate the package file

    return: str
    """
    project_folder = os.path.basename(os.path.normpath(os.getcwd()))
    if project_folder != 'Courier': os.chdir('..')
    for file in scan_dir(files=True, folders=False):
        if file.name == PACKAGE:
            return file
    logger.info("creating {green}{package}{reset} in {magenta}{cwd}{reset}".format(
        green=colorama.Fore.GREEN,
        reset=colorama.Fore.RESET,
        magenta=colorama.Fore.MAGENTA,
        cwd=os.getcwd(),
        package=PACKAGE))
    """
    with open('package.json', 'w', False, 'UTF-8') as fp:
        fp.
    """


def last_updated(_file):
    """ last update in datetime format

    returns: bool
    """
    pass

loc_package_file()
