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
from util import search_for_package

load_logging_ini()
logger = logging.getLogger()


def close(file):
    """ Close file in the case it\'s not closed """
    if not file.closed:
        file.close()


def read_docs(file='help.txt') -> list[str]:
    """ Read documentation file from folder """

    path = os.getcwd()
    # print(path)
    if not assert_file_path():
        print(os.getcwd())
        os.chdir('..')

    data = []

    with open(os.path.join('docs', file), 'r') as fp:
        data = fp.read().strip().splitlines()

    os.chdir(path)
    return data


def print_formatted_list(lines: list) -> None:
    """ Print list as a paragraph / string """
    for line in lines:
        print(line)


def proc_args(args: list = sys.argv[1:]):
    """ Get args and process them individually """
    if not len(args):
        print_formatted_list(read_docs(file="help.txt"))

    for argument in args:
        match argument:
            case '--help' | 'help':
                print_formatted_list(read_docs(file="help.txt"))
                return
            case '--do-nothing':
                return
            case 'get':
                match len(args):
                    case 1:
                        print("Syntax: courier get <package>")
                        return
                    case 2:
                        search_for_package(args[len(args) - 1])


def get_file_path() -> str:
    """ Rerurun immediate parent folder of current dir """
    return os.path.basename(os.path.normpath(os.getcwd()))


def assert_file_path() -> bool:
    """ Assert if file path is correct """
    new_file_path = get_file_path()
    return new_file_path == 'Courier'


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
