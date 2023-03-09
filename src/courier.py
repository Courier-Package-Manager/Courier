"""
Courier.courier
~~~~~~~~~~~~~~~

This module handles user input.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

from glob import glob
import logging
import os
import pathlib
import sys
from typing import Literal

import colorama

from util.codescan import Codescan
from util.package import Package
from util.update import load_logging_ini
from util.update import last_updated
from util.update import loc_package_file


def close_file(file):
    """Closes a file for unit testing.

    :param file: TextIOWrapper
    """

    if not file.closed:
        file.close()


def get_file_path():
    """Fetch immediate parent folder of current directory.

    :return: String 
    """

    return os.path.basename(os.path.normpath(os.getcwd()))


def assert_file_path() -> bool:
    """Assert if file path is set to the root directory name.

    :return: Boolean the root directory has been set.
    """

    new_file_path = get_file_path()
    return new_file_path == 'Courier'


def read_docs(file='help.txt'):
    """Read documentation file from folder.

    :param file: (optional) file from /docs as reference.
    :return: file contents excluding escape characters.
    :rtype: list[str]
    """

    path = os.getcwd()

    if not assert_file_path():
        logging.debug(Package.color_path(os.getcwd()))
        os.chdir('..')

    data = []

    # By using 'with' I can ensure that file is closed; thus avoiding
    # leaving open resources where there need not be any.
    with open(os.path.join('docs', file), 'r', encoding='utf') as _file:
        data = _file.read().strip().splitlines()
        close_file(_file)

    os.chdir(path)
    logging.debug(f" ✈️  Moving to {Package.color_path(os.getcwd())}")
    return data


def print_formatted_list(lines):
    """Print list as a paragraph.

    :param lines: List of strings removed of escape characters.
    """

    for line in lines:
        print(line)


def proc_args(args):
    """Process given command line arguments when Courier is called.

    :param args: List of CLI arguments, called through sys.argv()
    """

    for i in args:
        if i.endswith('.py'):
            args.remove(i)

    if len(args) == 0:
        print_formatted_list(read_docs(file="help.txt"))

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
                            return
                        case 'get':
                            print_formatted_list(read_docs(file="get.txt"))
                            return
                        case 'install':
                            print_formatted_list(read_docs(file="install.txt"))
                            return
                        case 'codescan':
                            print_formatted_list(read_docs(file="codescan.txt"))
                        case _:
                            print(f"Optional argument \'{args[1]}\' not found")
                            print("Run courier for a list of commands.")
                            return
            case '--do-nothing':
                return
            case 'codescan':
                if len(args) == 1:
                    # logger.info(" 🔎 Scanning for unmet dependencies ... ")
                    Codescan.install_dependencies()
                    return
            case 'install':
                if len(args) == 1:
                    print("Syntax: courier install <package> [version]")
                    return
                if len(args) == 2:
                    Package.update_package(args[args.index('install') + 1])
            case 'get':
                match len(args):
                    case 1:
                        print("Syntax: courier get <package>")
                        return
                    case 2:
                        Package.search(args[len(args) - 1])
                        return
            case _:
                print_formatted_list(read_docs(file="help.txt"))
                return


def get_package_created():
    """Format return value of the previous timestamp of update.json"""

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


def bashrc_exists() -> pathlib.Path | Literal[False]:
    """Locate (if present) the user bash configuration file.

    This function tests under the following directories:
        home/<user>/
        home/<user>/dotfiles/

    :return:
        :class:`pathlib.Path <Path>` object
        :class:`Literal <False>` boolean
    """

    for file in glob(os.path.join(str(pathlib.Path.home()), '*')):
        if 'bashrc' in file:
            return pathlib.Path(file)

    if os.path.exists(os.path.join(str(pathlib.Path.home()), 'dotfiles')):
        for file in glob(os.path.join(str(pathlib.Path.home()), 'dotfiles', '*')):
            if 'bashrc' in file:
                return pathlib.Path(file)
    return False


def add_bashrc_alias():
    """Eliminates need for 'python' prefix before file

    This function also removes the need for a '.py' suffix
    when calling courier.py. This alias references the src 
    directory such that 'src' is the working directory upon
    runtime. Courier will not work without this as multiple
    path locations and tests are configured around 'src'
    being the working runtime directory.
    """

    if exists:
        contents = []
        with open(bashrc_path, 'r') as file:
            contents = file.read().strip()
            file.close()

        file = os.path.join(os.getcwd(), "courier.py")

        # BUG can't be called globally for some reason?
        alias = f'alias courier={sys.executable} {file}'  

        if alias in contents:
            return

        with open(bashrc_path, 'a') as file:
            file.write('\n# Generated by Courier\n')
            file.write(f'{alias}\n')
            file.close()

        logger.debug(f" 👀 Added alias to {Package.color_path(str(bashrc_path))}")


load_logging_ini()
logger = logging.getLogger()

bashrc_path = bashrc_exists()
exists = bool(bashrc_path) != False

if exists:
    logger.debug(f" 📂 Found bashrc in {Package.color_path(str(bashrc_path))}")
    add_bashrc_alias()
else:
    logger.warning(" ❌ Could not find bashrc file. Courier may behave unexpectedly.")

main()
