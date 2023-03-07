"""
The MIT License (MIT)

Copyright (c) 2023 Joshua Rose

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

package.py has functions responsible for the following:
      - Indexing pypi database for release
      - Scanning for outdated packages
"""
# NOTE more to come soon...
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
        self.search_term = search_term # Term to be highlighted differently as it was explicitly searched for
        self.name           = Fore.CYAN + Package.get_name_from_lxml(li).text.strip()+ Fore.RESET     # pyright: ignore
        self.version        = Fore.LIGHTCYAN_EX + Package.get_version_from_lxml(li).text.strip()+ Fore.RESET  # pyright: ignore
        self.description    = Fore.LIGHTBLUE_EX + Package.get_desc_from_lxml(li).text.strip() + Fore.RESET    # pyright: ignore
        self.date           = Fore.LIGHTWHITE_EX + Package.get_date_from_lxml(li).text.strip()+ Fore.RESET     # pyright: ignore
        self.link           = f'https://pypi.org/project/{self.name}'
        self.id: int        = len(Package.packages) + 1                       # pyright: ignore

        if self.search_term in self.description:
            self.description = self.description.replace(self.search_term, Fore.LIGHTMAGENTA_EX + self.search_term + Fore.LIGHTBLUE_EX)

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
            print(f"{package.id} {package.name} {package.version} {package.date}")
            print(f"\t{package.description}")


def format_package_search_results(soup: BeautifulSoup, package):
    """ Organize all the results and remove the un-needed stuff """

    package_list = soup.select('.package-snippet') # pyright: ignore

    for element in package_list:
        Package.packages.append(Package(element, package))


def search_for_package(package: str):
    """
        Search for package in the pypi database.
        return: latest package version.
    """
    print(f" 🔎 Searching for {package}")
    soup = request_pypi_soup(package)

    # logging.info(f"Showing up to {max_results} results")
    format_package_search_results(soup, package)
    if not len(Package.packages):
        logging.critical(f" ❌ No results found for package \'{package}\'")
        sys.exit(0)
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


def service_online() -> bool:
    """ Check that pypi is online """
    try:
        pypi_request: object = requests.get('https://pypi.org')
        return pypi_request.status_code == 200
    except requests.RequestException as request_error:
        logging.critical(f"Ambiguous exception occurred: {str(request_error)}")
        sys.exit(1)


def run_quick_test():
    # logging.info(" 🕺 Getting pypi package details")
    search_for_package('pygame')
