#!/usr/bin/env python
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

from util.codescan import Codescan
from util.package import Package
from util.update import load_logging_ini
from util.update import loc_package_file


class Courier(object):
    """Handles user input and file IO."""

    def __init__(self):
        load_logging_ini()
        self.logger = logging.getLogger()

        self.bashrc_path = self.bashrc_exists()
        self.exists = bool(self.bashrc_path) != False

        if self.exists:
            self.logger.debug(
                f" 📂 Found bashrc in {Package.color_path(str(self.bashrc_path))}"
            )
            self.add_bashrc_alias()
        else:
            self.logger.warning(
                " ❌ Could not find bashrc file. Courier may behave unexpectedly."
            )

        self.proc_args(sys.argv)
        loc_package_file()

    @staticmethod
    def close_file(file):
        """Closes a file for unit testing.

        :param file: TextIOWrapper
        """

        if not file.closed:
            file.close()

    @staticmethod
    def get_file_path():
        """Fetch immediate parent folder of current directory.

        :return: String
        """

        return os.path.basename(os.path.normpath(os.getcwd()))

    @staticmethod
    def assert_file_path():
        """Assert if file path is set to the root directory name.

        :return: Boolean the root directory has been set.
        """

        new_file_path = Courier.get_file_path()
        return new_file_path == "Courier"

    @staticmethod
    def read_docs(file="help.txt"):
        """Read documentation file from folder.

        Colored documentation is going to be added, so I'm still
        finding a way to implement that, however it will be done.

        :param file: (optional) file from /docs as reference.
        :return: file contents excluding escape characters.
        :rtype: list[str]
        """

        path = os.getcwd()

        if Courier.assert_file_path() is not True:
            logging.debug(Package.color_path(os.getcwd()))
            os.chdir("..")

        data = []

        # By using 'with' I can ensure that file is closed; thus avoiding
        # leaving open resources where there need not be any.
        with open(os.path.join("docs", file), "r", encoding="utf") as _file:
            data = _file.read().strip().splitlines()
            Courier.close_file(_file)

        os.chdir(path)
        logging.debug(f" ✈️  Moving to {Package.color_path(os.getcwd())}")
        return data

    @staticmethod
    def print_formatted_list(lines):
        """Print list as a paragraph.

        :param lines: List of strings removed of escape characters.
        """

        for line in lines:
            print(line)

    @staticmethod
    def proc_args(args, get_test=False):
        """Process given command line arguments when Courier is called.

        :param args: List of CLI arguments, called through sys.argv()
        """

        for i in args:
            if i.endswith(".py"):
                args.remove(i)

        if len(args) == 0:
            Courier.print_formatted_list(Courier.read_docs(file="help.txt"))
            return

        for _, argument in enumerate(args):
            match argument:
                case "help":
                    if len(args) == 1:
                        Courier.print_formatted_list(Courier.read_docs(file="help.txt"))
                        return
                    if len(args) >= 2:
                        match args[args.index("help") + 1]:
                            case "--list" | "-l" | "list":
                                Courier.print_formatted_list(
                                    Courier.read_docs(file="menus.txt")
                                )
                                return
                            case "get" | "g":
                                Courier.print_formatted_list(
                                    Courier.read_docs(file="get.txt")
                                )
                                return
                            case "install" | "i":
                                Courier.print_formatted_list(
                                    Courier.read_docs(file="install.txt")
                                )
                                return
                            case "update" | "u" | "--update":
                                Courier.print_formatted_list(
                                    Courier.read_docs(file="update.txt")
                                )
                                return
                            case "codescan" | "cs" | "scan":
                                Courier.print_formatted_list(
                                    Courier.read_docs(file="codescan.txt")
                                )
                                return
                            case "--menu" | "menu":
                                if len(args) >= 3:
                                    match args[args.index("menu") + 1]:
                                        case "menu":
                                            Courier.print_formatted_list(
                                                Courier.read_docs(file="menus.txt")
                                            )
                                            return
                                        case "development":
                                            Courier.print_formatted_list(
                                                Courier.read_docs(
                                                    file="development.txt"
                                                )
                                            )
                                            return
                                        case "testing":
                                            Courier.print_formatted_list(
                                                Courier.read_docs(file="testing.txt")
                                            )
                                            return
                                        case "general":
                                            Courier.print_formatted_list(
                                                Courier.read_docs(file="help.txt")
                                            )
                                            return
                                        case "help":
                                            Courier.print_formatted_list(
                                                Courier.read_docs(file="help.txt")
                                            )
                                            return
                                        case _:
                                            Courier.print_formatted_list(
                                                Courier.read_docs(file="menus.txt")
                                            )
                                            return
                                else:
                                    Courier.print_formatted_list(
                                        Courier.read_docs(file="menus.txt")
                                    )
                                return
                            case "help":
                                print(
                                    "The help command displays mandatory and compulsary arguments for Courier."
                                )
                                return
                            case _:
                                print(f"Optional argument '{args[1]}' not found")
                                print("Run courier for a list of commands.")
                                return

                case "--do-nothing":
                    return

                case "--debug":
                    load_logging_ini("config_debug.ini")
                    Courier.print_formatted_list(Courier.read_docs(file="help.txt"))
                    return

                case "--clear":
                    os.system("clear")
                    Courier.print_formatted_list(Courier.read_docs(file="help.txt"))
                    return

                case "codescan":
                    match len(args):
                        case 1:
                            Codescan.install_dependencies()
                            return
                        case 2:
                            Courier.print_formatted_list(
                                Courier.read_docs(file="codescan.txt")
                            )
                            return
                case "install":
                    match len(args):
                        case 1:
                            print("Syntax: courier install <package> [version]")
                            return
                        case 2:
                            Package.update_package(args[args.index("install") + 1])
                            return
                        case 3:
                            Courier.print_formatted_list(
                                Courier.read_docs(file="install.txt")
                            )
                            return
                case "get":
                    match len(args):
                        case 1:
                            print("Syntax: courier get <package>")
                            return
                        case 2:
                            Package.search(args[len(args) - 1], get_test)
                            return
                        case 3:
                            Courier.print_formatted_list(
                                Courier.read_docs(file="get.txt")
                            )
                            return
                case _:
                    Courier.print_formatted_list(Courier.read_docs(file="help.txt"))
                    return

    def get_package_created(self):
        """Format return value of the previous timestamp of update.json"""

        Courier.assert_file_path()
        self.logger.debug("Package file %s update.json %s was created %s ")

    @staticmethod
    def bashrc_exists():
        """Locate (if present) the user bash configuration file.

        This function tests under the following directories:
            home/<user>/
            home/<user>/dotfiles/

        :return:
            :class:`pathlib.Path <Path>` object
            :class:`Literal <False>` boolean
        """

        for file in glob(os.path.join(str(pathlib.Path.home()), "*")):
            if "bashrc" in file:
                return pathlib.Path(file)

        if os.path.exists(os.path.join(str(pathlib.Path.home()), "dotfiles")):
            for file in glob(os.path.join(str(pathlib.Path.home()), "dotfiles", "*")):
                if "bashrc" in file:
                    return pathlib.Path(file)
        return False

    def add_bashrc_alias(self):
        """Eliminates need for 'python' prefix before file

        This function also removes the need for a '.py' suffix
        when calling courier.py. This alias references the src
        directory such that 'src' is the working directory upon
        runtime. Courier will not work without this as multiple
        path locations and tests are configured around 'src'
        being the working runtime directory.
        """

        if self.exists:
            contents = []
            with open(self.bashrc_path, "r") as file:
                contents = file.read().strip()
                file.close()

            file = os.path.join(os.getcwd(), "courier.py")

            # BUG can't be called globally for some reason?
            alias = f"alias courier={sys.executable} {file}"

            if alias in contents:
                return

            with open(self.bashrc_path, "a") as file:
                file.write("\n# Generated by Courier\n")
                file.write(f"{alias}\n")
                file.close()

            self.logger.debug(
                f" 👀 Added alias to {Package.color_path(str(self.bashrc_path))}"
            )


courier = Courier()
