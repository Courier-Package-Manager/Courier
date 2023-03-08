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
import os
import sys
import colorama
from update import load_logging_ini
from update import last_updated
from update import loc_package_file
from package import Package

load_logging_ini()
logger = logging.getLogger()


def close(file):
    """ Close file in the case it\'s not closed """
    if not file.closed:
        file.close()

def get_file_path() -> str:
    """ Rerurun immediate parent folder of current dir """
    return os.path.basename(os.path.normpath(os.getcwd()))


def assert_file_path() -> bool:
    """ Assert if file path is correct """
    new_file_path = get_file_path()
    return new_file_path == 'Courier'


def read_docs(file='help.txt') -> list[str]:
    """ Read documentation file from folder """

    path = os.getcwd()
    logger.debug(path)
    # print(path)
    if not assert_file_path():
        logging.debug(Package.color_path(os.getcwd()))
        os.chdir('..')

    data = []

    with open(os.path.join('docs', file), 'r', encoding='utf') as _file:
        data = _file.read().strip().splitlines()

    os.chdir(path)
    logging.debug(f" ✈️  Changing dir to {Package.color_path(os.getcwd())}")
    return data


def print_formatted_list(lines: list) -> None:
    """ Print list as a paragraph / string """
    for line in lines:
        print(line)
    return


def proc_args(args: list):
    """ Get args and process them individually """

    for i in args:
        if i.endswith('.py'):
            args.remove(i)

    if len(args) == 0:
        print_formatted_list(read_docs(file="help.txt"))

    # logger.debug(args)

    for argument in args:
        match argument:
            case '--help' | 'help':
                print_formatted_list(read_docs(file="help.txt"))
                return
            case '--do-nothing':
                return
            case 'codescan':
                if len(args) == 1:
                    logger.info("  🔎 Scanning for unmet dependencies ... ")
            case 'install':
                if len(args) == 1:
                    print("Syntax: courier install <package> [version]")
                    return;
                if len(args) == 2:
                    Package.update_package(args[args.index('install') + 1])
            case 'get':
                match len(args):
                    case 1:
                        print("Syntax: courier get <package>")
                        return
                    case 2:
                        Package.search(args[len(args) - 1])
                        return;
            case _:
                print_formatted_list(read_docs(file="help.txt"))
                return
                



def get_package_created() -> None:
    """ Prints the date that update.json was created """
    assert_file_path()
    logger.debug("Package file %s update.json %s was created %s ",
                 colorama.Fore.GREEN,
                 colorama.Fore.RESET,
                 last_updated())
    return


def main():
    """Currently calling functions for testing"""
    proc_args(sys.argv)
    loc_package_file()


# Package.auto_install()
main()
