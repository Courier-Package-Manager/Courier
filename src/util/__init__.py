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

Description: Initializes anything it can before importing utils such as colors
and testing whatever utils will need, in this case network.
"""

import sys
import logging
import colorama

from .package import Package  # pyright: ignore
from .update import get_project_folder
from .update import loc_package_file
from .update import last_updated
from .update import scan_dir
from .update import update_packages
from .update import load_logging_ini
from .update import get_date
from .codescan import Codescan

load_logging_ini()
logger = logging.getLogger()

colorama.init()

# NOTE this is to satisfy flake errors, serves no practical purpose
__locals__ = [
    get_project_folder,
    loc_package_file,
    get_date,
    Codescan,
    last_updated,
    scan_dir,
    update_packages,
    load_logging_ini,
]


def display_if_online(url) -> bool:
    """ Display if pypi is online """
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

# TODO figure out why this is displayed AFTER Codescan() logs
display_if_online('https://pypi.org') 

# Codescan.install_dependencies()
