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

import logging
import unittest

from requests.exceptions import MissingSchema

from util.package import Package

logger = logging.getLogger()


class TestUnitPackageClass(unittest.TestCase):
    """ Test unit package class object """

    def setUp(self):
        """ Set up instances & instance variables """
        self.soup = Package.request_pypi_soup('test')
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_get_name_from_lxml(self):
        """ Test get name from lxml """
        Package.get_name_from_lxml(self.soup)

    def test_get_version_from_lxml(self):
        """ Test get version from lxml """
        Package.get_version_from_lxml(self.soup)

    def test_get_date_from_lxml(self):
        """ Test get date from lxml """
        Package.get_date_from_lxml(self.soup)

    def test_get_desc_from_lxml(self):
        """ Get get description from lxml """
        Package.get_desc_from_lxml(self.soup)

    def test_name_from_id(self):
        """ Index packages for name testing each ones id """
        Package.search('pygame')
        Package.id_from_name(Package.packages[0].name)

    def test_install_from_id(self):
        """ Test install from id """
        for i in range(-1, 2):
            Package.install_from_id(i, unittest=True)
            Package.install_from_id(i, unittest=False)
        Package.install_from_id(-1, unittest=False)

    def test_id_from_name(self):
        """ Index packages for id testing each ones name """
        Package.search('pygame')
        Package.id_from_name(Package.packages[0].name)

    def test_format_results(self):
        """ Test format package search results """
        for package in Package.packages:
            Package.format_results(package, "")

    def test_search(self):
        """ Test search for package """
        Package.search('openpyxl')
        Package.search('colorama', True)

    def test_request_pypi_soup(self):
        """ Test request pypi soup """
        Package.request_pypi_soup('matplotlib')

    def test_service_online(self):
        """ Test service online """
        with self.assertRaises(MissingSchema) as _:
            Package.service_online(url='TestRequestException')

    def test_is_installed(self):
        """ Test is installed """
        Package.is_installed('numpy')

    def test_query_install_install(self):
        """ Test query install w/ input """
        self.assertEqual(Package.query_install(True), True)

    def test_update_package(self):
        """ Test update package with pip """


if __name__ == '__main__':
    unittest.main()
