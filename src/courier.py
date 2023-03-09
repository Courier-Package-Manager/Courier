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
import pathlib
import sys
from glob import glob
from typing import Literal

import colorama

from util import Codescan
from util.package import Package
from util.update import load_logging_ini
from util.update import last_updated
from util.update import loc_package_file

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

    if not assert_file_path():
        logging.debug(Package.color_path(os.getcwd()))
        os.chdir('..')

    data = []

    with open(os.path.join('docs', file), 'r', encoding='utf') as _file:
        data = _file.read().strip().splitlines()

    os.chdir(path)
    logging.debug(f" ✈️  Moving to {Package.color_path(os.getcwd())}")
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
            case 'help':
                if len(args) == 1:
                    print_formatted_list(read_docs(file="help.txt"))
                    return
                elif len(args) == 2:
                    match args[1]:
                        case '--list' | '-l':
                            print_formatted_list(read_docs(file="menus.txt"))
                            return;
                        case 'get':
                            print_formatted_list(read_docs(file="get.txt"))
                            return;
                        case 'install':
                            print_formatted_list(read_docs(file="install.txt"))
                            return;
                        case _:
                            print(f"Optional argument \'{args[1]}\' not found")
                            print("Run courier for a list of commands.")
                            return;
            case '--do-nothing':
                return
            case 'codescan':
                if len(args) == 1:
                    logger.info(" 🔎 Scanning for unmet dependencies ... ")
                    return;
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
# Ensure that courier is a command in bashrc


def bashrc_exists() -> pathlib.Path | Literal[False]:
    """ tests bashrc exists in ~/bashrc | ~/.bashrc | ~/dotfiles/* """ 
    for file in glob(os.path.join(str(pathlib.Path.home()), '*')):
        if 'bashrc' in file:
            return pathlib.Path(file)

    if os.path.exists(os.path.join(str(pathlib.Path.home()), 'dotfiles')):
        for file in glob(os.path.join(str(pathlib.Path.home()), 'dotfiles', '*')):
            if 'bashrc' in file:
                return pathlib.Path(file)
    return False

bashrc_path = bashrc_exists()
exists = bool(bashrc_path) != False

def add_bashrc_alias():
    """ Adds alias so that python courier.py is shortened to courier """
    if exists:
        contents = []
        with open(bashrc_path, 'r') as file:
            contents = file.read().strip()
            file.close()

        alias = r'alias courier="python courier.py"' 

        if alias in contents:
            return;

        with open(bashrc_path, 'a') as file:
            file.write('\n# Generated by Courier\n')
            file.write(f'{alias}\n')
            file.close()

        logger.debug(f" 👀 Added alias to {Package.color_path(str(bashrc_path))}")
        return;
    

if exists:
    logger.debug(f" 🔎 Found bashrc in {Package.color_path(str(bashrc_path))}")
    add_bashrc_alias()
else:
    logger.warning("Could not find bashrc file. Courier may behave unexpectedly.")

main()
