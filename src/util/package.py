""" Has functions responsible for the following:
     - Indexing pypi database for release
     - scanning for outdated packages
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
logger.level = logging.INFO


class Package(object):
    """ Structure for Package """
    def __init__(self, li) -> None:
        self.name: Tag | None = Package.get_name_from_lxml(li)
        self.version: Tag | None = Package.get_version_from_lxml(li)
        self.description: Tag | None = Package.get_date_from_lxml(li)
        self.link: Tag | None = Package.get_desc_from_lxml(li)
        self.date: Tag | None = Package.get_date_from_lxml(li)

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


def format_package_search_results(soup: BeautifulSoup):
    """ Organize all the results and remove the un-needed stuff """
    packages = []
    package_container = soup.find('ul', class_='unstyled')
    package_list = package_container.find_all('li') # pyright: ignore

    for element in package_list:
        if isinstance(element, NoneType):
            print(element)
            continue

        # logger.debug(element)

        try:
            lxml = BeautifulSoup(element, 'lxml')
        except TypeError:
            continue

        package = Package(lxml)
        packages.append(package)


def search_for_package(package: str, max_results=10):
    """
        Search for package in the pypi database.
        return: latest package version.
    """
    logging.info(f" 🔎 Searching pypi for {package}")
    soup = request_pypi_soup(package)

    logging.info(f"Showing up to {max_results} results")
    results = format_package_search_results(soup)
    if not results:
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
