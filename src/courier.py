# -*- coding=utf-8 -*-
# TODO add docstrings to file functions
# TODO relocate file functions
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

import logging
import colorama
import sys
import os

from util import load_logging_ini
from util import loc_package_file
from util import last_updated

load_logging_ini()
logger = logging.getLogger()


def proc_args(args: list = sys.argv):
    """ Get args and process them individually """
    logger.debug(assert_file_path())
    if not assert_file_path():
        logger.debug(os.getcwd())
        os.chdir('..')
        logger.debug(os.getcwd())
    for argument in args:
        match argument:
            case '--help' | 'help':
                os.popen(f'cat {os.path.join("docs", "help.txt")} | less', mode='r').readlines()


def get_file_path() -> str:
    """ Rerurun immediate parent folder of current dir """
    return os.path.basename(os.path.normpath(os.getcwd()))


def assert_file_path() -> bool:
    """ Assert if file path is correct """
    new_file_path = get_file_path()
    logging.debug(new_file_path)
    return new_file_path == 'Courier'


"""
if file_path != 'Courier':
    logger.debug(assert_file_path())
"""


def get_package_created() -> None:
    """ Prints the date that update.json was created """
    assert_file_path()
    logger.debug("Package file {m}update.json{r} was created {d}".format(
        m=colorama.Fore.GREEN,
        r=colorama.Fore.RESET,
        d=last_updated()))


def main():
    """Currently calling functions for testing"""
    proc_args()
    loc_package_file()


main()
