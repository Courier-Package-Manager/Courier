"""
Courier.util.package
~~~~~~~~~~~~~~~~~~~~

This module holds the `Package` class
which is used as a part dataclass part
syntax convention to execute both utility
and core methods.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

import logging
import os
import pathlib
import subprocess
import sys
from typing import Literal

from bs4 import BeautifulSoup
import colorama
from colorama import Fore
import requests

from .setup import escape_ansi
from .update import load_logging_ini


class Package(object):
    """Basic container for both singular and compound packages. Package regulates
    global package functions and reades files etc. Packages are often least used
    in a multi-instance context which is likely noticeable from the amount of staticmethods.
    """

    packages = []

    def __init__(self, li, search_term) -> None:
        # Term to be highlighted differently as it
        # was explicitly searched for
        search_term = search_term
        if not li:
            return
        if not search_term:
            return

        lxml_name = Package.get_name_from_lxml(li)
        lxml_date = Package.get_date_from_lxml(li)
        lxml_desc = Package.get_desc_from_lxml(li)
        lxml_ver = Package.get_version_from_lxml(li)

        if not lxml_name:
            return
        if not lxml_date:
            return
        if not lxml_desc:
            return
        if not lxml_ver:
            return

        name = lxml_name.text.strip()
        date = lxml_date.text.strip()
        desc = lxml_desc.text.strip()
        ver = lxml_ver.text.strip()

        self.name = "{color}{name}{reset}".format(
            color=Fore.CYAN, name=name, reset=Fore.RESET
        )
        self.version = "{color}{name}{reset}".format(
            color=Fore.LIGHTCYAN_EX, name=ver, reset=Fore.RESET
        )
        self.date = "{color}{name}{reset}".format(
            color=Fore.LIGHTCYAN_EX, name=date, reset=Fore.RESET
        )
        self.description: str = "{color}{name}{reset}".format(
            color=Fore.BLUE, name=desc, reset=Fore.RESET
        )
        self._description = self.description.replace(
            search_term, Fore.LIGHTMAGENTA_EX + search_term + Fore.LIGHTBLUE_EX
        )
        self.id = len(Package.packages) + 1

    @staticmethod
    def get_name_from_lxml(lxml: BeautifulSoup):
        """Returns mutable BeautifulSoup object from a specified HTML class.

        :param lxml: Data structure representing an HTML element as a `BeautifulSoup` object
        :return: BeautifulSoup tag that is part of a parse tree
        """

        return lxml.select_one(".package-snippet__name")

    @staticmethod
    def get_version_from_lxml(lxml: BeautifulSoup):
        """Returns mutable BeautifulSoup object from a specified HTML class.

        :param lxml: Data structure representing an HTML element as a `BeautifulSoup` object
        :return: BeautifulSoup tag that is part of a parse tree
        """

        return lxml.select_one(".package-snippet__version")

    @staticmethod
    def get_date_from_lxml(lxml: BeautifulSoup):
        """Returns mutable BeautifulSoup object from a specified HTML class.

        :param lxml: Data structure representing an HTML element as a `BeautifulSoup` object
        :return: BeautifulSoup tag that is part of a parse tree
        """

        return lxml.select_one(".package-snippet__created time")

    @staticmethod
    def get_desc_from_lxml(lxml: BeautifulSoup):
        """Returns mutable BeautifulSoup object from a specified HTML class.

        :param lxml: Data structure representing an HTML element as a `BeautifulSoup` object
        :return: BeautifulSoup tag that is part of a parse tree
        """

        return lxml.select_one(".package-snippet__description")

    @classmethod
    def list(cls):
        """Display packages fetched from pypi with syntax formatting.

        :param limit: The maximum amount as an Integer of packages to be displayed
        :return: The success state of the function
        :rtype: bool
        """

        cls.packages.reverse()

        for _, package in enumerate(cls.packages):
            print(
                "{id} {name} {version} {date}\n\t{description}".format(
                    id=package.id,
                    name=package.name,
                    version=package.version,
                    date=package.date,
                    description=package.description,
                )
            )

        return True

    @staticmethod
    def name_from_id(id: int) -> str | Literal[False]:
        """Compare package ID to `id`.

        Only returns package name if package `id`
        and the packge id are equal.

        :param id: An Integer of the package ID to get name from.
        :return: An integer of the package ID if package ID is equal to `id`
        :rtype: str | Literal[False]
        """

        for package in Package.packages:
            if package.id == id:
                return package.name
            else:
                continue
        return False

    @staticmethod
    def id_from_name(name: str) -> int | Literal[False]:
        """Compare package name to `name`.

        Only returns package ID if package name and `name` are equal.

        :param name: A string of the package name to get ID from.
        :return: A string of the package name if package name is equal to `name`
        :rtype: int | Literal[False]
        """

        for package in Package.packages:
            if package.name == name:
                return package.id
            else:
                continue
        return False

    @staticmethod
    def format_results(soup: BeautifulSoup, package: str):
        """Sort a given html element and convert into parseable format.

        :param soup: BeautifulSoup html element to be sorted through.
        :param package: A given package to be added to list `Package.packages`
        :return: If the given soup has the 'select' attribute.
        :rtype: bool
        """

        if hasattr(soup, "select"):
            package_list = soup.select(".package-snippet")
            for element in package_list:
                Package.packages.append(Package(element, package))
                continue
            return True
        else:
            return False

    @staticmethod
    def package_info(selector: str | int):
        """Get package info from pypi.

        :param selector: If string then get the package name, if int then get the id of
        the last cached search. Note that str is mandatory if previous cache has been
        cleared.
        """

        match str(type(selector)):
            case str(str()):
                package = Package.packages[Package.packages.index(selector)]
            case str(int()):
                if len(Package.packages) == 0:
                    logging.warning(
                        "Cannot search by ID: no cache present from previous search."
                    )
                    return
                else:
                    package = Package.packages[
                        Package.packages.index(Package.name_from_id(int(selector)))
                    ]
                    return
            case _:
                logging.warning(
                    f"Datatype {type(selector)} is not supported as an indexer to a package."
                )
                return

        LOGGER.info(
            """
              Package: {package_name}
              Date: {package_date}
              Version: {package_version}
              Description: {package_description}""".format(
                package_name=package.name,
                package_date=package.date,
                package_version=package.version,
                package_description=package.description,
            )
        )

    @staticmethod
    def install_from_id(id: int | None, unittest=False):
        """Install a package from given list.

        This function matches the `id` parameter to a given
        package that has been listed. It does this through
        the `Package.name_from_id` method. This can also
        be done in the opposite way as `Package.id_from_name`.

        :param id: An integer of a listed package.
        :param unittest: Boolean in the case of unit testing.
        """

        # In the case that no package has been selected, simply return as NULL.
        if id == 0:
            return

        package_count = len(Package.packages)

        if not package_count:
            LOGGER.critical(
                colorama.Fore.RED
                + " ❌ Could not index package list; no cache loaded."
                + colorama.Fore.RESET
            )
            return

        LOGGER.debug(
            f" loaded {colorama.Fore.GREEN + str(package_count) + colorama.Fore.RESET} packages."
        )
        if isinstance(id, int):
            if isinstance(Package.name_from_id(id), str):
                package = Package.name_from_id(id)
            else:
                LOGGER.error(" ❌ No package specified")
                return
        else:
            return

        if not package:
            return
        elif unittest:
            logging.debug(""" 🧪 Not doing anything due to unit test mock permissions""")
        else:
            # remove formatting
            package = escape_ansi(package)
            os.system(f"{sys.executable} -m pip install {package}")
            return

    @staticmethod
    def query_install_input(unittest: bool) -> int:
        """Query user input to select package to install.

        :param unittest: Boolean value used in case of coverage.
        :return: The user selected package ID from displayed packages.
        :rtype: int
        """

        if not unittest:
            selected = input(" ==> ")
            return int(selected)
        else:
            # Return statement is to assert in the case of a unit test
            # that the return type is an integer instance and the numeric
            # value of the return type meets any ID presented to the user
            # which corresponds to a listed package.
            print("Unit test flag called")
            return 1

    @staticmethod
    def handle_query_input(selected: str | int, unittest: bool):
        """An indicator of whether a package is to be installed.

        :param selected: A python dependency parsed as a String or ID.
        :param unittest: Boolean value used as coverage.
        :return: If a package is to be installed based on shown criteria.
        :rtype: boolean
        """

        match selected:
            case "":
                return False
            case _:
                Package.install_from_id(int(selected), unittest)
                return True

    @staticmethod
    def query_install(unittest: bool):
        """Query the install ID of a given package.

        the package.Packages.packages (list) variable,
        the user may query an associated (int) ID to install
        a package which is converted to a string in ai
        `Package` class method.

        :param unittest: Boolean value used as coverage
        :return: If exception caught from user input
        :rtype: boolean
        """

        try:
            selected = Package.query_install_input(unittest)
            Package.handle_query_input(selected, unittest)
            return True
        except Exception as error:
            logging.error(str(error))
            return False

    @staticmethod
    def search(package: str, activate_test_case=False):
        """Search for package in the pypi database.

        :param package: Package name as string.
        :param activate_test_case: (optional) Used for unit test coverage.
        :return: If search yields results (which is most of the time will)
        :rtype: bool
        """

        LOGGER.info(
            f" 🔎 {colorama.Fore.LIGHTCYAN_EX}Searching for {package} {colorama.Fore.RESET}"
        )
        soup = Package.request_pypi_soup(package)

        Package.format_results(soup, package)

        if not len(Package.packages):
            logging.critical(f" ❌ No results found for package '{package}'")
            return False

        Package.list()  # Display fetched packages with special formatting.
        id = Package.query_install_input(activate_test_case)
        Package.install_from_id(id, activate_test_case)

    @staticmethod
    def request_pypi(package: str):
        """Request an HTTP response for `package`

        :param package: A URL of a python package, typically matching
            that of a pypi package url.
        :return: Server response to requested URL `package`
        :rtype: requests.Response
        """

        pypi_request = requests.get(f"https://pypi.org/search/?q={package}")

        return pypi_request

    @staticmethod
    def request_pypi_soup(package: str) -> BeautifulSoup:
        """Requests a soup object from a pypy package URL.

        :param package: A URL of a python package, typically matching
            that of a pypi package url.
        :return: BeautifulSoup data structure representing an html element.
        :rtype: bs4.BeautifulSoup
        """

        pypi_request = Package.request_pypi(package)
        soup = BeautifulSoup(pypi_request.content, "html.parser")
        return soup

    @staticmethod
    def service_online(url="https://pypi.org"):
        """This function checks if the specified URL is online.

        :param url: URL String to be used as a request object.
        :return: Status code of request matches online status code (200)
        :rtype: bool
        """

        pypi_request = requests.get(url)
        return pypi_request.status_code == 200

    @staticmethod
    def auto_install(root="."):
        """Read all non-local imports `root` recursively.

        This function reads all files recursively while excluding
        specified folders which are set as exclusions.

        :param root: (optional) Root directory as string.
        :return: A list of files that match the given quota
        :rtype: list[str]
        """

        files = []
        ignore = [".git", ".github", "libs", ".tox", "venv", "htmlcov"]

        path = pathlib.Path(root)

        sizes = {
            "small": {
                "color": colorama.Fore.BLUE,
                "icon": "📘",
                "min": 0,
                "max": 999,
            },
            "medium": {
                "color": colorama.Fore.RED,
                "icon": "📕",
                "min": 1000,
                "max": 9999,
            },
            "large": {
                "color": colorama.Fore.GREEN,
                "icon": "📗",
                "min": 10000,
                "max": 99999,
            },
            "chunky": {
                "color": colorama.Fore.YELLOW,
                "icon": "📙",
                "min": 100000,
                "max": 999999,
            },
        }

        LOGGER.debug(
            f"""\n
                📘 = {colorama.Fore.LIGHTCYAN_EX}small{colorama.Fore.RESET}
                📕 = {colorama.Fore.RESET}medium{colorama.Fore.RESET}
                📗 = {colorama.Fore.GREEN}large{colorama.Fore.RESET}
                📙 = {colorama.Fore.YELLOW}chunky{colorama.Fore.RESET} \n"""
        )

        for file in path.rglob("*.py"):
            head, _ = os.path.join(file.parent, file.name).split("/", 1)
            if head in ignore:
                continue
            files.append(file)

        files = sorted(files, key=os.path.getsize, reverse=True)

        for file in files:
            filesize = os.path.getsize(file)

            for size in sizes:
                if filesize in range(sizes[size]["min"], sizes[size]["max"]):
                    icon = sizes[size]["icon"]
                    color = sizes[size]["color"]
                    null = colorama.Fore.RESET
                    LOGGER.debug(f"{color} {icon} {str(file)}{null}")
        return files

    @staticmethod
    def color_path(path=os.getcwd()):
        """Changes the color of each folder in `path` relative to a list preset of colors.

        :param path: (optional) Path as string which must contain at least two directories.
        :return: A list of path components that are then concatenated.
        :rtype: String
        """

        components = path.split("/", path.count("/"))
        colors = [
            Fore.GREEN,
            Fore.RED,
            Fore.MAGENTA,
            Fore.CYAN,
            Fore.YELLOW,
            Fore.BLUE,
            Fore.LIGHTGREEN_EX,
            Fore.LIGHTRED_EX,
            Fore.LIGHTMAGENTA_EX,
            Fore.LIGHTCYAN_EX,
            Fore.LIGHTYELLOW_EX,
            Fore.LIGHTBLUE_EX,
        ]

        color_index = 0

        for index, component in enumerate(components):
            if color_index > len(colors):
                color_index = 0

            match index:
                case 0:
                    components[index] = colors[color_index - 1] + component + Fore.RESET
                case _:
                    components[index] = (
                        colors[color_index - 1] + "/" + component + Fore.RESET
                    )

            # Incrementing color index then switches to the next color in list `colors`.
            color_index += 1

        return "".join(components)

    @staticmethod
    def update_cache(package: str):
        """Sends results to cache but does not display or query input

        :param package: Name of package to add to cache.
        """
        LOGGER.debug(
            f" 📦 {colorama.Fore.LIGHTWHITE_EX} Refreshing package cache {colorama.Fore.RESET}"
        )
        Package.packages.clear()
        LOGGER.info(
            f" 🔎 {colorama.Fore.LIGHTCYAN_EX}Searching for {package} {colorama.Fore.RESET}"
        )
        soup = Package.request_pypi_soup(package)
        Package.format_results(soup, package)

        if not len(Package.packages):
            logging.critical(f" ❌ No results found for package '{package}'")
            return False

    @staticmethod
    def update_package(package: str):
        """Updates `package` to latest or specified version with pip.

        :param package: A string that matches a pypi supported dependency

        :return: Returns if the operation was successful or not in
            updating `package`.
        :rtype: bool
        """

        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError:
            logging.warning("Waning: failed to install package.")
            return
        return


load_logging_ini()
LOGGER = logging.getLogger()
