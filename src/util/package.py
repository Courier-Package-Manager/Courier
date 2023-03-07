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
import sys

from bs4 import BeautifulSoup
import requests

from colorama import Fore

logger = logging.getLogger()
logger.level = logging.INFO


class Package(object):
    """ Structure for Package """
    packages = []

    def __init__(self, li, search_term) -> None:
        # Term to be highlighted differently as it
        # was explicitly searched for
        search_term = search_term 
        _name = Package.get_name_from_lxml(
                li).text.strip()  # pyright: ignore
        version = Package.get_version_from_lxml(
                li).text.strip()  # pyright: ignore
        date = Package.get_date_from_lxml(
                li).text.strip()  # pyright: ignore
        description = Package.get_desc_from_lxml(
                li).text.strip()  # pyright: ignore
        self.name = "{color}{name}{reset}".format(
                color = Fore.CYAN,
                name=_name,
                reset = Fore.RESET)
        self.version = "{color}{name}{reset}".format(
                color = Fore.LIGHTCYAN_EX,
                name=version,
                reset = Fore.RESET)
        self.date = "{color}{name}{reset}".format(
                color = Fore.LIGHTCYAN_EX,
                name=date,
                reset = Fore.RESET)
        self.description = "{color}{name}{reset}".format(
                color = Fore.BLUE,
                name=description,
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
    def show_packages(cls):
        """ Display packages fetched from pypi with syntax formatting """
        cls.packages.reverse()
        for package in cls.packages:
            print("{id} {name} {version} {date}\n\t{description}".format(
                id=package.id,
                name=package.name,
                version=package.version,
                date=package.date,
                description=package.description))


def format_package_search_results(soup: BeautifulSoup, package):
    """ Organize all the results and remove the un-needed stuff """

    if hasattr(soup, 'select'):
        package_list = soup.select('.package-snippet')

        for element in package_list:
            Package.packages.append(Package(element, package))


def search_for_package(package: str, activate_test_case=False):
    """
        Search for package in the pypi database.
        return: latest package version.
    """
    print(f" 🔎 Searching for {package}")
    soup = request_pypi_soup(package)

    # logging.info(f"Showing up to {max_results} results")
    format_package_search_results(soup, package)

    if not len(Package.packages) or activate_test_case:
        logging.critical(f" ❌ No results found for package \'{package}\'")
        return
    logger.debug(f' {len(Package.packages)} packages found')
    Package.show_packages()


def request_pypi(package) -> requests.Response:
    """ Returns pypi request object """
    pypi_request = requests.get(f'https://pypi.org/search/?q={package}')
    return pypi_request


def request_pypi_soup(package) -> BeautifulSoup:
    """ Give me the soup 🍜 """
    pypi_request = request_pypi(package)
    soup = BeautifulSoup(pypi_request.content, 'html.parser')
    return soup


def service_online(url='https://pypi.org') -> bool:
    """ Check that pypi is online """
    pypi_request: object = requests.get(url)
    return pypi_request.status_code == 200