"""
source: Courier.util.package
test: tests.test_unit_package_class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module tests the `Package` class
which is used as a part dataclass part
syntax convention to execute both utility
and core methods.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

import os
import logging
import unittest

from requests.exceptions import MissingSchema

from util.package import Package

logger = logging.getLogger()


class TestUnitPackageClass(unittest.TestCase):
    """ Test unit package class object """

    def setUp(self):
        """ Set up instances & instance variables """
        print(f" 🌟 {self.__doc__}")
        self.soup = Package.request_pypi_soup('test')
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG
        os.system('clear')

    def test_get_name_from_lxml(self):
        """ Test get name from lxml """
        print(f" 🌟 {self.__doc__}")
        Package.get_name_from_lxml(self.soup)
        os.system('clear')

    def test_get_version_from_lxml(self):
        """ Test get version from lxml """
        print(f" 🌟 {self.__doc__}")
        Package.get_version_from_lxml(self.soup)
        os.system('clear')

    def test_get_date_from_lxml(self):
        """ Test get date from lxml """
        print(f" 🌟 {self.__doc__}")
        Package.get_date_from_lxml(self.soup)
        os.system('clear')

    def test_get_desc_from_lxml(self):
        """ Get get description from lxml """
        print(f" 🌟 {self.__doc__}")
        Package.get_desc_from_lxml(self.soup)
        os.system('clear')

    def test_name_from_id(self):
        """ Index packages for name testing each ones id """
        print(f" 🌟 {self.__doc__}")
        Package.search('pygame')
        Package.id_from_name(Package.packages[0].name)
        os.system('clear')

    def test_install_from_id(self):
        """ Test install from id """
        print(f" 🌟 {self.__doc__}")
        for i in range(-1, 2):
            Package.install_from_id(i, unittest=True)
            Package.install_from_id(i, unittest=False)
        Package.install_from_id(-1, unittest=False)
        os.system('clear')

    def test_id_from_name(self):
        """ Index packages for id testing each ones name """
        print(f" 🌟 {self.__doc__}")
        Package.search('pygame')
        Package.id_from_name(Package.packages[0].name)
        os.system('clear')

    def test_format_results(self):
        """ Test format package search results """
        print(f" 🌟 {self.__doc__}")
        for package in Package.packages:
            Package.format_results(package, "")
        os.system('clear')

    def test_search(self):
        """ Test search for package """
        print(f" 🌟 {self.__doc__}")
        Package.search('openpyxl')
        Package.search('colorama', True)
        os.system('clear')

    def test_request_pypi_soup(self):
        """ Test request pypi soup """
        print(f" 🌟 {self.__doc__}")
        Package.request_pypi_soup('matplotlib')
        os.system('clear')

    def test_service_online(self):
        """ Test service online """
        os.system('clear')
        print(f" 🌟 {self.__doc__}")
        with self.assertRaises(MissingSchema) as _:
            Package.service_online(url='TestRequestException')

    def test_is_installed(self):
        """ Test is installed """
        os.system('clear')
        print(f" 🌟 {self.__doc__}")
        Package.search('numpy')
        os.system('clear')
        Package.search('numpy', activate_test_case=True)
        os.system('clear')

    def test_query_install_install(self):
        """ Test query install w/ input """
        os.system('clear')
        print(f" 🌟 {self.__doc__}")
        self.assertEqual(Package.query_install(True), True)


if __name__ == '__main__':
    os.system('clear')
    print(f" 🧪 Testing {os.getcwd()}")
    unittest.main()
