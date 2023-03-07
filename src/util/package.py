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

from datetime import datetime
import logging
import sys
from types import NoneType

from bs4 import BeautifulSoup
from bs4.element import Tag
import requests

logger = logging.getLogger()
logger.level = logging.DEBUG


class Package(object):
    """ Structure for Package """
    packages = []
    def __init__(self, li) -> None:
        self.name: Tag | None = Package.get_name_from_lxml(li).text
        self.version: Tag | None = Package.get_version_from_lxml(li).text
        self.description: Tag | None = Package.get_date_from_lxml(li)
        self.link: Tag | None = Package.get_desc_from_lxml(li)
        self.date: Tag | None = Package.get_date_from_lxml(li)
        self.id: int = len(Package.packages)

    @staticmethod
    def get_name_from_lxml(lxml: BeautifulSoup):
        return lxml.select_one('.package-snippet__name')

    @staticmethod
    def get_version_from_lxml(lxml: BeautifulSoup):
        return lxml.select_one('.package-snippet__version')
    
    @staticmethod
    def get_date_from_lxml(lxml: BeautifulSoup):
        return lxml.select_one('.package-snippet__created span time')

    @staticmethod
    def get_desc_from_lxml(lxml: BeautifulSoup):
        return lxml.select_one('.package-snippet__description')

    @staticmethod
    def get_link_from_lxml(lxml: BeautifulSoup):
        return lxml.select_one('a href')

    @classmethod
    def show_packages(cls):
        cls.packages.reverse()
        for package in cls.packages:
            print(f"{package.id} {package.name} {package.version}")
            print(f"\t{package.description}")



def format_package_search_results(soup: BeautifulSoup):
    """ Organize all the results and remove the un-needed stuff """

    package_container = soup.find('ul', class_='unstyled')
    package_list = package_container.find_all('li') # pyright: ignore

    for element in package_list:
        Package.packages.append(Package(element))


def search_for_package(package: str, max_results=10):
    """
        Search for package in the pypi database.
        return: latest package version.
    """
    logging.info(f" 🔎 Searching pypi for {package}")
    soup = request_pypi_soup(package)

    logging.info(f"Showing up to {max_results} results")
    format_package_search_results(soup)
    logger.debug(f' {len(Package.packages)} packages found')
    for package in Package.packages:
        print(package.name)
    if not len(Package.packages):
        logging.critical(f" ❌ No results found for package \'{package}\'")
        sys.exit(0)


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
    logging.info(" 🕺 Getting pypi package details")
    search_for_package('pygame')
