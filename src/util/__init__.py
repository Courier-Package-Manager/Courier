"""
Courier.util.__init__
~~~~~~~~~~~~~~~~~~~~~

This module initializes required dependencies
as well as adds relative imports to the global
directory variable as references.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

import logging
import sys

import colorama

from .codescan import Codescan
from .package import Package
from .update import get_project_folder
from .update import loc_package_file
from .update import last_updated
from .update import scan_dir
from .update import load_logging_ini
from .update import get_date


def display_if_online(url):
    """Queries url for response code

    :param url: String supporting a utf-8 url format.
    :return: If the specified url is online.
    :rtype: bool
    """

    up = False
    try:
        if Package.service_online(url):
            up = True
    finally:
        if up:
            logger.debug(f" 🌍 {url} is up!")
        else:
            logging.critical(f" 🌐 {url} is down")
            sys.exit(1)
        return up


__modules__ = [
    get_project_folder,
    loc_package_file,
    get_date,
    Codescan,
    last_updated,
    scan_dir,
    load_logging_ini,
]

load_logging_ini()
logger = logging.getLogger()

colorama.init()

display_if_online('https://pypi.org') 
