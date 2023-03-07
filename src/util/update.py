import os
import json
from types import EllipsisType
from typing import IO, Any, Literal
from .setup import get_date
from posix import DirEntry
from datetime import datetime
import logging
import colorama

from logging.config import fileConfig

logger = logging.getLogger()

PACKAGE = 'update.json'
GREEN = colorama.Fore.GREEN
RESET = colorama.Fore.RESET
MAGENTA = colorama.Fore.MAGENTA

cwd = os.getcwd()


def file_exists(file, mode) -> str | bool:
    """ Test if file exists (recurring snippet) """
    try:
        file = open(file, mode)
        file.close()
        return file
    except FileNotFoundError:
        return False


def last_updated():
    """ last update in datetime format.
     This is assuming that the following code has run:
     >>> if project_folder != 'Courier': os.chdir('..')
    """
    if file_exists(PACKAGE, 'r'):
        data = json.load(open(PACKAGE, 'r'))
        timestamp = datetime.fromtimestamp(data['created'])
        date = get_date(timestamp)
        return date


def load_logging_ini() -> None:
    """ Load logging ini file """
    fileConfig('config.ini')


def update_packages() -> EllipsisType:
    """ The core function of this entire repo """
    # TODO auto read python files and add dependencies
    return ...


def scan_dir(files=True, folders=True) -> list[DirEntry]:
    """
    A better version of the os.scandir function,
    as it takes multiple args.
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
    """ Dedicate function for testing """
    project_folder = os.path.basename(os.path.normpath(os.getcwd()))
    return project_folder


def switch_root() -> str:
    """ Auto switch root when not applicable """
    project_folder = get_project_folder()
    if project_folder != 'Courier':
        os.chdir('..')
    return project_folder


def create_package() -> None:
    """ Create package and dump json to said package """

    with open(PACKAGE, 'w', True, 'UTF-8') as fp:
        ts = datetime.now().timestamp()
        data = {
            "created": ts,
            "dependencies": {}
        }
        json.dump(data, fp)
        fp.close()


def get_package_name() -> DirEntry | None:
    """ Get package name / allows for unit tests """
    switch_root()  # Switch root before asking if its in the switched directory
    for file in scan_dir(files=True, folders=False):
        if file.name == PACKAGE:
            return file


def loc_package_file(
        name=get_package_name(),
        debug=False,
        mode='r') -> IO[Any] | None:
    """ Locate the package file & create package file if it doesn't exist. """
    if not name or debug:
        logger.info(f"Set {GREEN}{PACKAGE}{RESET} in {MAGENTA}{cwd}{RESET}")
        return create_package()
    else:
        with open(PACKAGE, mode) as fp:
            try:
                return fp
            finally:
                if 'w' in list(mode):
                    fp.close()
