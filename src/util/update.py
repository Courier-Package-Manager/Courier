"""
Courier.util.update
~~~~~~~~~~~~~~~~~~~~

This modules is reponsible for updating Courier as
a program. This module is also responsibile for
utility functions and the management of aesthetic
dependencies such as colorama and logging.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

from datetime import datetime
import json
import logging
from logging.config import fileConfig
import os
from posix import DirEntry
from typing import Any, IO, Literal

import colorama

from .setup import get_date


def file_exists(file: str, mode: str) -> None | bool:
    """Test if file exists in the current working directory

    :param file: Filename as a string
    :param mode: Given filemode eg: read, write, append (as char)
    :return: False if file is not present or TextIOWrapper if present
    :rtype: False | TextIOWrapper
    """

    try:
        _file = open(file, mode)
        try:
            if isinstance(_file, bool):
                return _file
        finally:
            _file.close()
    except FileNotFoundError:
        print( "file not found")
        return;


def last_updated() -> str | Literal[False]:
    """last update in datetime format

    This is assuming that
         >>> if project_folder != 'Courier': os.chdir('..')
    has run as this function is dependant on the current
    working directory containing the `PACKAGE` file.

    :return: Current date as a timestamp
    :rtype: string
    """

    if file_exists('update.json', 'r'):
        with open('update.json', 'r') as _file:
            data = json.load(_file)
            _file.close()
        timestamp = datetime.fromtimestamp(data['created'])
        date = get_date(timestamp)
        return date
    else:
        return False


def load_logging_ini(config='config_info.ini') -> None:
    """Load logging configuration file"""
    fileConfig(config)


def scan_dir(files=True, folders=True) -> list[DirEntry]:
    """A better version of the os.scandir function, as it takes multiple args.

    :param files: (optional) List files in current directory
    :param folders: (optional) List folders in current directory
    :return: A list of current files and folders found
    :rtype: list[DirEntry]
    """

    items = []

    for item in os.scandir(os.getcwd()):
        items.append(item)
    if not files:
        [items.remove(item) for item in items if os.path.isfile(item)]
    if not folders:
        [items.remove(item) for item in items if os.path.isdir(item)]

    return items


def get_project_folder() -> str:
    """Dedicated function for testing

    :return: The current project folder name.
    :rtype: str
    """

    project_folder = os.path.basename(os.path.normpath(os.getcwd()))
    return project_folder


def switch_root() -> str:
    """Auto switch root when not applicable

    :return: Full current project path as a String
    :rtype: string
    """

    project_folder = get_project_folder()
    if project_folder != 'Courier':
        os.chdir('..')
    return project_folder


def create_package() -> None:
    """Dump json object to `PACKAGE`
    raises permissions error if user
    does not have write permissions to current
    working directory.
    """

    try:
        with open('update.json', 'w', True, 'UTF-8') as fp:
            ts = datetime.now().timestamp()
            data = {
                "created": ts,
                "dependencies": {}
            }
            json.dump(data, fp)
            fp.close()
    except PermissionError:
        raise PermissionError


def get_package_name() -> DirEntry | None:
    """Get package name.

    Note that this function also allows for unit tests.

    :return: A directory entry of the current file.
    :rtype: DirEntry | None
    """

    switch_root()  # Switch root before asking if its in the switched directory
    for file in scan_dir(files=True, folders=False):
        if file.name == 'update.json':
            return file


def loc_package_file(
        name=get_package_name(),
        debug=False,
        mode='r') -> IO[Any] | None:
    """Locate the package file & create package file 

    If the file does not exist it will be created in the current
    working directory of wherever `courier.py` was called from.

    :param name: DirEntry of current package name as file
    :param debug: If a unit test is to be conducted allow for artifically invoked edge cases.
    :param mode: Edit mode of file to be called as read, write or append.
    :return: File object if package has been opened or None
    :rtype: FileIOWrapper | None
    """

    if not name or debug:
        logger.info(f"Set {GREEN}'update.json'{RESET} in {MAGENTA}{cwd}{RESET}")
        return create_package()
    else:
        with open('update.json', mode) as fp:
            try:
                try:
                    return fp
                finally:
                    fp.close()
            finally:
                if 'w' in list(mode):
                    fp.close()


logger = logging.getLogger()

GREEN = colorama.Fore.GREEN
RESET = colorama.Fore.RESET
MAGENTA = colorama.Fore.MAGENTA

cwd = os.getcwd()
