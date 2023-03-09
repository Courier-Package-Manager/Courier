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
from typing import Literal, Self, Type

from bs4 import BeautifulSoup
import colorama
from colorama import Fore
from packaging import version
import pkg_resources
import requests

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

        _name = lxml_name.text.strip()
        date = lxml_date.text.strip()
        desc = lxml_desc.text.strip()
        ver = lxml_ver.text.strip()

        self.name = "{color}{name}{reset}".format(
                color = Fore.CYAN,
                name=_name,
                reset = Fore.RESET)
        self.version = "{color}{name}{reset}".format(
                color = Fore.LIGHTCYAN_EX,
                name=ver,
                reset = Fore.RESET)
        self.date = "{color}{name}{reset}".format(
                color = Fore.LIGHTCYAN_EX,
                name=date,
                reset = Fore.RESET)
        self.description = "{color}{name}{reset}".format(
                color = Fore.BLUE,
                name=desc,
                reset = Fore.RESET)
                    
        self.id = len(Package.packages) + 1

        if search_term in self.description:
            self.description = self.description.replace(
                    search_term, Fore.LIGHTMAGENTA_EX + search_term + Fore.LIGHTBLUE_EX)

    @staticmethod
    def get_name_from_lxml(lxml: BeautifulSoup):
        """Returns mutable BeautifulSoup object from a specified HTML class.

        :param lxml: Data structure representing an HTML element as a `BeautifulSoup` object
        :return: BeautifulSoup tag that is part of a parse tree
        """

        return lxml.select_one('.package-snippet__name')

    @staticmethod
    def get_version_from_lxml(lxml: BeautifulSoup):
        """Returns mutable BeautifulSoup object from a specified HTML class.

        :param lxml: Data structure representing an HTML element as a `BeautifulSoup` object
        :return: BeautifulSoup tag that is part of a parse tree
        """

        return lxml.select_one('.package-snippet__version')
    
    @staticmethod
    def get_date_from_lxml(lxml: BeautifulSoup):
        """Returns mutable BeautifulSoup object from a specified HTML class.

        :param lxml: Data structure representing an HTML element as a `BeautifulSoup` object
        :return: BeautifulSoup tag that is part of a parse tree
        """

        return lxml.select_one('.package-snippet__created time')

    @staticmethod
    def get_desc_from_lxml(lxml: BeautifulSoup):
        """Returns mutable BeautifulSoup object from a specified HTML class.

        :param lxml: Data structure representing an HTML element as a `BeautifulSoup` object
        :return: BeautifulSoup tag that is part of a parse tree
        """

        return lxml.select_one('.package-snippet__description')

    @classmethod
    def list(cls: Type[Self], limit=10):
        """Display packages fetched from pypi with syntax formatting.

        :param limit: The maximum amount of packages to be displayed
        :return: The success state of the function
        :rtype: bool
        """

        cls.packages.reverse()

        for index, package in enumerate(cls.packages):
            if index >= limit:
                return False

            print("{id} {name} {version} {date}\n\t{description}".format(
                id=package.id,
                name=package.name,
                version=package.version,
                date=package.date,
                description=package.description))

        return True

    @staticmethod
    def name_from_id(id: str) -> str | Literal[False]:
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

        if hasattr(soup, 'select'):
            package_list = soup.select('.package-snippet')
            for element in package_list:
                Package.packages.append(Package(element, package))
                continue
            return True
        else:
            return False

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
        if id is False:
            return

        package_count = len(Package.packages)
        
        # If not_package_count is cleaner to me and shorter
        # than doing the more common but verbose 'if package == ...'
        if not package_count:
            LOGGER.critical(" ❌ Could not index package list; no cache loaded")
            return

        LOGGER.debug(f'loadeded {package_count} packages.')
        if isinstance(Package.name_from_id, int):
            package = Package.name_from_id(id)
        else:
            raise TypeError

        if not package:
            return
        elif unittest:
            logging.debug(" 🧪 Not doing anything due to unit test mock permissions")
            return
        else:
            os.system(f'{sys.executable} -m pip install {package.name}')
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

        Once packages have been listed and stored in 
        the package.Packages.packages (list) variable,
        the user may query an associated (int) ID to install
        a package which is converted to a string in a 
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
            logging.debug(str(error))
            return False

    @staticmethod
    def search(package: str, activate_test_case=False):
        """Search for package in the pypi database.

        :param package: Package name as string.
        :param activate_test_case: (optional) Used for unit test coverage.
        :return: If search yields results (which is most of the time will)
        :rtype: bool
        """

        print(f" 🔎 Searching for {package}")
        soup = Package.request_pypi_soup(package)

        LOGGER.debug(" 📦 Refreshing package cache")
        Package.packages.clear()

        Package.format_results(soup, package)

        if not len(Package.packages) or activate_test_case:
            logging.critical(f" ❌ No results found for package \'{package}\'")
            return False

        # NOTE log removed as it won't be seen most of the time as searching packages
        # often turns up with more results that the size of the screen making the 
        # log pointless as it would not be visible 90% of the time one searches for 
        # any given package. (NOTE response quantity varies by package quantity obv)
        # LOGGER.debug(f' 🔎 {len(Package.packages)} packages found')

        Package.list()  # Display fetched packages with special formatting.
        return True

    @staticmethod
    def request_pypi(package: str):
        """Request an HTTP response for `package` 

        :param package: A URL of a python package, typically matching
            that of a pypi package url. 
        :return: Server response to requested URL `package`
        :rtype: requests.Response
        """

        pypi_request = requests.get(f'https://pypi.org/search/?q={package}')

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
        soup = BeautifulSoup(pypi_request.content, 'html.parser')
        return soup

    @staticmethod
    def service_online(url='https://pypi.org'):
        """This function checks if the specified URL is online.

        :return: Status code of request matches online status code (200)
        :rtype: bool
        """

        pypi_request: object = requests.get(url)
        return pypi_request.status_code == 200

    @staticmethod
    def auto_install(root='.'):
        """Read all non-local imports `root` recursively.

        This function reads all files recursively while excluding
        specified folders which are set as exclusions.

        :param root: (optional) Root directory as string.
        :return: A list of files that match the given quota
        :rtype: list[str]
        """

        files = []
        ignore = ['.git', '.github', 'libs', '.tox', 'venv', 'htmlcov']

        path = pathlib.Path(root)

        sizes = {
                "small": {
                    "color": colorama.Fore.BLUE,
                    "icon": '📘',
                    "min": 0,
                    "max": 999,
                    },
                "medium": {
                    "color": colorama.Fore.RED,
                    "icon": '📕',
                    "min": 1000,
                    "max": 9999,
                    },
                "large": {
                    "color": colorama.Fore.GREEN,
                    "icon": '📗',
                    "min": 10000,
                    "max": 99999,
                    },
                "chunky": {
                    "color": colorama.Fore.YELLOW,
                    "icon": '📙',
                    "min": 100000,
                    "max": 999999
                    },
                }

        # LOGGER.debug(" 🔎 Recursively scanning for unmet dependencies")
        LOGGER.debug(f"""\n
                📘 = small | 📕 = medium | 📗 = large | 📙 = chunky \n""")

        for file in path.rglob('*.py'):
            head, _ = os.path.join(file.parent, file.name).split('/', 1)
            if head in ignore:
                continue
            files.append(file)

        for file in path.rglob('*'):
            head, _ = os.path.join(file.parent, file.name).split('/', 1)
            if head in ignore:
                continue
            if os.path.isdir(file):
                files.append(file)

        files = sorted(files, key=os.path.getsize, reverse=True)

        for file in files:

            filesize = os.path.getsize(file)

            for size in sizes:
                if filesize in range(sizes[size]["min"], sizes[size]["max"]):

                    icon  = sizes[size]["icon"]
                    color = sizes[size]["color"]

                    null  = colorama.Fore.RESET

                    LOGGER.debug(f"{color} {icon} {str(file)}{null}")  # pyright: ignore
        return files

    @staticmethod
    def color_path(path=os.getcwd()):
        """Changes the color of each folder in `path` relative to a list preset of colors.

        :param path: (optional) Path as string which must contain at least two directories.
        :return: A list of path components that are then concatenated.
        :rtype: String
        """

        components = path.split('/', path.count('/'))
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
                Fore.LIGHTBLUE_EX]

        color_index = 0

        # If the color list is reached then end then
        # return to the start of the list as to not
        # run into an `IndexError`.
        for index, component in enumerate(components):
            if color_index > len(colors):
                color_index = 0

            match index:
                case 0:
                    components[index] = colors[color_index - 1] + \
                            component + Fore.RESET
                case _:
                    components[index] = colors[color_index - 1] + \
                            '/' + component + Fore.RESET

            # Incrementing color index then switches
            # to the next color in list `colors`.
            color_index += 1

        return ''.join(components)

    @staticmethod
    def update_package(package: str, _version: bool | str = False):
        """Updates `package` to latest or specified version with pip.

        :param package: A string that matches a pypi supported dependency
        :param version: (optional) The version of `package` to be
            installed. If none is given, `package` is updated to the latest
            version.
        :return: Returns if the operation was successful or not in
            updating `package`.
        :rtype: bool
        """

        packs = {}
        exists = True

        if _version:
            _ver = version.parse(str(_version))

        for i in pkg_resources.working_set:
            packs[i.key] = i.parsed_version

        try:
            LOGGER.debug(_ver.__str__)  # pyright: ignore
            exists = False
        except NameError:
            pass

        if package in packs.keys():
<<<<<<< HEAD
            if _version != False:
                if _ver < packs[package]: # pyright: ignore
                    LOGGER.info(f"""
 📦 You already have {package} installed, however it is out of date.""") # pyright: ignore
=======
            if _version != False and exists:

                # pyright gives an error that _ver is 
                # possibly unbound, however this cannot
                # ever happen as this is checked before hand
                # and is stored as an `exists` boolean
                if _ver < packs[package]:  # pyright: ignore
                    LOGGER.info(f" 📦 You already have {package} installed, however it is out of date.") # pyright: ignore
>>>>>>> 5d9b1993 (📝 Add extensive documentation strings based off of requests documentation)
                    LOGGER.info(f" ⏫ Updating {package} to version {_ver}") # pyright: ignore
                    subprocess.check_call([
                        sys.executable, "-m", "pip", "install", f"{package}=={_ver.__str__()}"]) # pyright: ignore
                    return True
                else:
                    subprocess.check_call([
                        sys.executable, "-m", "pip", "install", f"{package}"])
                    return True
            else:
                LOGGER.info(f" ✅ You already have the latest version of {package}")
                return True
        else:
            return False


load_logging_ini()
LOGGER = logging.getLogger()
