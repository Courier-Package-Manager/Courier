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

from bs4 import BeautifulSoup
from colorama import Fore
import requests

logger = logging.getLogger()
logger.level = logging.INFO


class Package(object):
    """ Structure for Package """
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
            return;
        if not lxml_date:
            return;
        if not lxml_desc:
            return;
        if not lxml_ver:
            return;

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
    def list(cls):
        """ Display packages fetched from pypi with syntax formatting """
        cls.packages.reverse()
        for package in cls.packages:
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
        if not id:
            return # NOTE no package selected
        package_count = len(Package.packages)
        if package_count == 0:
            logger.critical("Could not index package list, as no cache has been loaded")
            return
        logger.debug(f'loadeded {package_count} packages.')
        package: None | Package = Package.name_from_id(id)
        if not package:
            return;
        if unittest:
            logging.debug("Not doing anything due to unit test mock permissions.")
            return
        else:
            os.system(f'python -m pip install {package.name}')
            return

    @staticmethod
    def query_install_input():
        """ Primarily used for unit testing """
        selected = input(" ==> ")
        return selected

    @staticmethod
    def handle_query_input(selected):
        """ Handle given input """
        match selected:
            case "":
                return False
            case _:
                Package.install_from_id(int(selected))
                return True

    @staticmethod
    def query_install():
        """ Install package from id """
        # logging.debug(" .. Install package #%s" % Fore.LIGHTMAGENTA_EX)
        while 1:
            try:
                selected = Package.query_install_input()
                Package.handle_query_input(selected)
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

        logger.debug("Refreshing package cache")
        Package.packages.clear()

        # logging.info(f"Showing up to {max_results} results")
        Package.format_results(soup, package)

        if not len(Package.packages) or activate_test_case:
            logging.critical(f" ❌ No results found for package \'{package}\'")
            return
        logger.debug(f' {len(Package.packages)} packages found')
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
    def auto_install(root_dir):
        """
        1. Look in files to auto-install package
        2. Prune un-needed files
        """

        files = []
        # NOTE dirs to ignore
        # TODO set to actual loadable config dir
        ignore = ['.git', '.github', 'libs']

        subdirs = [file[0] for file in os.walk(os.path.abspath(root_dir ))]
        for subdir in subdirs:
            if os.path.split(subdir)[1] in ignore:
                continue
            subdir_files = os.walk(subdir).__next__()[2]
            if (len(subdir_files) > 0):
                for file in subdir_files:
                    path = Package.color_path(os.path.join(subdir, file))
                    logger.debug(f''' Found: {path} ''')
                    files.append(os.path.join(subdir, file))


    @staticmethod
    def color_path(path: str = os.getcwd()):
        """
            Desc: Stupid function i don't know why I made this
                  It just makes pathnames rainbow
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
            if color_index > len(colors):
                color_index = 0

            match index:
                case 0:
                    components[index] = colors[color_index - 1] + \
                            component + Fore.RESET
                case _:
                    components[index] = colors[color_index - 1] + \
                            '/' + component + Fore.RESET
            color_index += 1

        return ''.join(components)
