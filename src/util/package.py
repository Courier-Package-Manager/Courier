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

package.py has functions responsible for the following:
      - Indexing pypi database for release
      - Scanning for outdated packages
"""

import logging
import os
import sys
import colorama
from packaging import version
import pkg_resources
from bs4 import BeautifulSoup
from colorama import Fore
import requests
import pathlib
import subprocess

from .update import load_logging_ini

load_logging_ini()
LOGGER = logging.getLogger()

class Package(object):
    """ 
        Basic container for both singular and 
        compound packages. Package regulates
        global package functions and reades
        files etc. Packages are often least used
        in a multi-instance context which is likely
        noticeable from the amount of staticmethods.
    """
    packages = []

    def __init__(self, li, search_term) -> None:
        # Term to be highlighted differently as it
        # was explicitly searched for
        search_term = search_term 
        if not li: return
        if not search_term: return
        lxml_name = Package.get_name_from_lxml(li)
        lxml_date = Package.get_date_from_lxml(li)
        lxml_desc = Package.get_desc_from_lxml(li)
        lxml_ver = Package.get_version_from_lxml(li)

        # NOTE this allows functions that would never be covered to 
        #      seem covered under the coverage package.
        if not lxml_name: return
        if not lxml_date: return
        if not lxml_desc: return
        if not lxml_ver: return

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
                    
        self.id: int = len(Package.packages) + 1

        if search_term in self.description:
            self.description = self.description.replace(
                    search_term,
                    Fore.LIGHTMAGENTA_EX + search_term + Fore.LIGHTBLUE_EX)

    @staticmethod
    def get_name_from_lxml(lxml: BeautifulSoup):
        return lxml.select_one('.package-snippet__name')

    @staticmethod
    def get_version_from_lxml(lxml: BeautifulSoup):
        return lxml.select_one('.package-snippet__version')
    
    @staticmethod
    def get_date_from_lxml(lxml: BeautifulSoup):
        return lxml.select_one('.package-snippet__created time')

    @staticmethod
    def get_desc_from_lxml(lxml: BeautifulSoup):
        return lxml.select_one('.package-snippet__description')

    @classmethod
    def list(cls, limit=10):
        """ Display packages fetched from pypi with syntax formatting """
        cls.packages.reverse()
        for index, package in enumerate(cls.packages):
            if index >= limit:
                return
            print("{id} {name} {version} {date}\n\t{description}".format(
                id=package.id,
                name=package.name,
                version=package.version,
                date=package.date,
                description=package.description))

    @staticmethod
    def name_from_id(id):
        for package in Package.packages:
            if package.id == id:
                return package

    @staticmethod
    def id_from_name(name):
        for package in Package.packages:
            if package.name == name:
                return package


    @staticmethod
    def format_results(soup: BeautifulSoup, package):
        """ Organize all the results and remove the un-needed stuff """

        if hasattr(soup, 'select'):
            package_list = soup.select('.package-snippet')

            for element in package_list:
                Package.packages.append(Package(element, package))

    @staticmethod
    def is_installed(_):
        pass

    @staticmethod
    def install_from_id(id: int | None, unittest=False):
        """ run pip to install package from id """
        if not id: return # NOTE no package selected
        package_count = len(Package.packages)
        if package_count == 0:
            LOGGER.critical(\
""" ❌ Could not index package list, as no cache has been loaded""")
            return
        LOGGER.debug(f'loadeded {package_count} packages.')
        package: None | Package = Package.name_from_id(id)
        if not package:
            return
        if unittest:
            logging.debug(\
""" 🧪 Not doing anything due to unit test mock permissions.""")
            return
        else:
            os.system(f'python -m pip install {package.name}')
            return

    @staticmethod
    def query_install_input(unittest) -> int:
        """ Primarily used for unit testing """
        if not unittest:
            selected = input(" ==> ")
            return int(selected)
        return 1

    @staticmethod
    def handle_query_input(selected, unittest):
        """ Handle given input """
        match selected:
            case "": return False
            case _:
                Package.install_from_id(int(selected), unittest)
                return True

    @staticmethod
    def query_install(unittest):
        """ Install package from id """
        # logging.debug(" .. Install package #%s" % Fore.LIGHTMAGENTA_EX)
        while 1:
            try:
                selected = Package.query_install_input(unittest)
                Package.handle_query_input(selected, unittest)
                return True
            except Exception as error:
                logging.debug(str(error))
                return False

    @staticmethod
    def search(package: str, activate_test_case=False):
        """
            Search for package in the pypi database.
            return: latest package version.
        """
        print(f" 🔎 Searching for {package}")
        soup = Package.request_pypi_soup(package)

        LOGGER.debug(" 📦 Refreshing package cache")
        Package.packages.clear()

        Package.format_results(soup, package)

        if not len(Package.packages) or activate_test_case:
            logging.critical(f" ❌ No results found for package \'{package}\'")
            return
        LOGGER.debug(f' 🔎 {len(Package.packages)} packages found')
        Package.list()


    @staticmethod
    def request_pypi(package) -> requests.Response:
        """ Returns pypi request object """
        pypi_request = requests.get(f'https://pypi.org/search/?q={package}')
        return pypi_request


    @staticmethod
    def request_pypi_soup(package) -> BeautifulSoup:
        """ Give me the soup 🍜 """
        pypi_request = Package.request_pypi(package)
        soup = BeautifulSoup(pypi_request.content, 'html.parser')
        return soup


    @staticmethod
    def service_online(url='https://pypi.org') -> bool:
        """ Check that pypi is online """
        pypi_request: object = requests.get(url)
        return pypi_request.status_code == 200


    @staticmethod
    def auto_install(root='.'):
        """
        root: root directory

        1. Look in files to auto-install package
        2. Prune un-needed files

        todo(feat): writing to config file
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

        LOGGER.debug(" 🔎 Recursively scanning for unmet dependencies")
        LOGGER.debug(f"""\n
                📘 = small | 📕 = medium | 📗 = large | 📙 = chunky \n""")
        for file in path.rglob('*.py'):
            head, base = os.path.join(file.parent, file.name).split('/', 1)  # pyright: ignore
            if head in ignore:
                continue
            files.append(file)

        for file in path.rglob('*'):
            head, base = os.path.join(file.parent, file.name).split('/', 1)  # pyright: ignore
            if head in ignore: continue
            if os.path.isdir(file): files.append(file)

        files = sorted(files, key=os.path.getsize, reverse=True)

        for file in files:
            filesize = os.path.getsize(file)
            for size in sizes:
                if filesize in range(sizes[size]["min"], sizes[size]["max"]):
                    icon = sizes[size]["icon"]
                    color = sizes[size]["color"]
                    null = colorama.Fore.RESET
                    LOGGER.debug(f"{color} {icon} {str(file)}{null}")  # pyright: ignore
        return files

    @staticmethod
    def color_path(path: str = os.getcwd()):
        """
            Desc: Stupid function i don't know why I made this
                  It just makes path names rainbow
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

        for index, component in enumerate(components):
            if color_index > len(colors): color_index = 0

            match index:
                case 0:
                    components[index] = colors[color_index - 1] + \
                            component + Fore.RESET
                case _:
                    components[index] = colors[color_index - 1] + \
                            '/' + component + Fore.RESET
            color_index += 1

        return ''.join(components)

    @staticmethod
    def update_package(package, _version: bool | str = False) -> bool:
        """ Update package with pip """

        '''
        def tuple_to_version(_ver: tuple) -> version.Version:  # pyright: ignore
            """ Convert tuple to version """
            _ver_str = ''
            for num in _ver: _ver_str += num + '.'
            return Version(_ver_str[:1])
        '''

        packs = {}

        if _version:
            _ver = version.parse(str(_version))

        for i in pkg_resources.working_set:
            packs[i.key] = i.parsed_version

        """
        exists = True
        try:
            LOGGER.debug(_ver.__str__)
            exists = False
        except NameError:
        """

        if package in packs.keys():
            if _version != False:
                if _ver < packs[package]: # pyright: ignore
                    LOGGER.info(f" 📦 You already have {package} installed, however it is out of date.") # pyright: ignore
                    LOGGER.info(f" ⏫ Updating {package} to version {_ver}") # pyright: ignore
                    subprocess.check_call([
                        sys.executable,
                        "-m",
                        "pip",
                        "install",
                        f"{package}=={_ver.__str__()}"]) # pyright: ignore
                    return True
                subprocess.check_call([
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    f"{package}"])
                return True
            else:
                LOGGER.info(f" ✅ You already have the latest version of {package}")
                return True
        return False
