import os
import json
from .setup import get_date
from posix import DirEntry
from datetime import datetime
import logging
import colorama

from logging.config import fileConfig

logger = logging.getLogger()

PACKAGE = 'update.json'


def last_updated():
    """ last update in datetime format. """
    # NOTE this is assuming that the following code has run:
    # >>> if project_folder != 'Courier': os.chdir('..')
    data = json.load(open(PACKAGE, 'r'))
    timestamp = datetime.fromtimestamp(data['created'])
    date = get_date(timestamp)
    return date


def load_logging_ini():
    """ Load logging ini file """
    fileConfig('../config.ini')

def update_packages():
    """ The core function of this entire repo """
    # TODO auto read python files and add dependencies
    ...


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


def switch_root():
    """ Auto switch root when not applicable """
    project_folder = os.path.basename(os.path.normpath(os.getcwd()))
    if project_folder != 'Courier':
        os.chdir('..')


def create_package():
    """ Create package and dump json to said package """

    with open(PACKAGE, 'w', True, 'UTF-8') as fp:
        ts = datetime.now().timestamp()
        data = {
            "created": ts,
            "dependencies": {}
        }
        json.dump(data, fp)
        fp.close()


def loc_package_file():
    """ Locate the package file & create package file if it doesn't exist. """
    switch_root()  # Switch root before asking if its in the switched directory
    for file in scan_dir(files=True, folders=False):
        if file.name == PACKAGE:
            return file

    logger.info(" 📨 Creating {G}{P}{R} in {M}{C}{R}".format(
        G=colorama.Fore.GREEN,
        R=colorama.Fore.RESET,
        M=colorama.Fore.MAGENTA,
        C=os.getcwd(),
        P=PACKAGE))

    create_package()
