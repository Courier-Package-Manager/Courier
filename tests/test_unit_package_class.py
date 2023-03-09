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
        self.soup = Package.request_pypi_soup('test')
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG
        os.system('clear')

    def test_get_name_from_lxml(self):
        """ Test get name from lxml """
        Package.get_name_from_lxml(self.soup)
        os.system('clear')

    def test_get_version_from_lxml(self):
        """ Test get version from lxml """
        Package.get_version_from_lxml(self.soup)
        os.system('clear')

    def test_get_date_from_lxml(self):
        """ Test get date from lxml """
        Package.get_date_from_lxml(self.soup)
        os.system('clear')

    def test_get_desc_from_lxml(self):
        """ Get get description from lxml """
        Package.get_desc_from_lxml(self.soup)
        os.system('clear')

    def test_name_from_id(self):
        """ Index packages for name testing each ones id """
        Package.search('pygame')
        Package.id_from_name(Package.packages[0].name)
        os.system('clear')

    def test_install_from_id(self):
        """ Test install from id """
        for i in range(-1, 2):
            Package.install_from_id(i, unittest=True)
            Package.install_from_id(i, unittest=False)
        Package.install_from_id(-1, unittest=False)
        os.system('clear')

    def test_id_from_name(self):
        """ Index packages for id testing each ones name """
        Package.search('pygame')
        Package.id_from_name(Package.packages[0].name)
        os.system('clear')

    def test_format_results(self):
        """ Test format package search results """
        for package in Package.packages:
            Package.format_results(package, "")
        os.system('clear')

    def test_search(self):
        """ Test search for package """
        Package.search('openpyxl')
        Package.search('colorama', True)
        os.system('clear')

    def test_request_pypi_soup(self):
        """ Test request pypi soup """
        Package.request_pypi_soup('matplotlib')
        os.system('clear')

    def test_service_online(self):
        """ Test service online """
        with self.assertRaises(MissingSchema) as _:
            Package.service_online(url='TestRequestException')
        os.system('clear')

    def test_is_installed(self):
        """ Test is installed """
        Package.search('numpy')
        os.system('clear')
        Package.search('numpy', activate_test_case=True)
        os.system('clear')

    def test_query_install_install(self):
        """ Test query install w/ input """
        self.assertEqual(Package.query_install(True), True)
        os.system('clear')

    def test_update_package(self):
        """ Test update package with pip """


if __name__ == '__main__':
    os.system('clear')
    print(f" 🧪 Testing {os.getcwd()}")
    unittest.main()
