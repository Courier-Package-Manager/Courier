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
import logging
import unittest
from unittest.mock import patch

from requests.exceptions import MissingSchema

from util.package import Package

logger = logging.getLogger()


class TestUnitPackageClass(unittest.TestCase):
    """ Test unit package class object """
    def setUp(self):
        """ Set up instances & instance variables """
        self.package = 'tensorflow'
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
        Package.search(self.package)
        Package.id_from_name(Package.packages[0].name)

    def test_install_from_id(self):
        """ Test install from id """
        Package.install_from_id(0, unittest=True)

    def test_id_from_name(self):
        """ Index packages for id testing each ones name """
        Package.search(self.package)
        Package.id_from_name(Package.packages[0].name)

    def test_format_results(self):
        """ Test format package search results """
        for package in Package.packages:
            Package.format_results(package, "")

    def test_search(self):
        """ Test search for package """
        Package.search(self.package)
        Package.search(self.package, True)

    def test_request_pypi_soup(self):
        """ Test request pypi soup """
        Package.request_pypi_soup(self.package)

    def test_service_online(self):
        """ Test service online """
        with self.assertRaises(MissingSchema) as _:
            Package.service_online(url='TestRequestException')

    def test_is_installed(self):
        """ Test is installed """
        Package.is_installed(self.package)

    @patch('util.Package.query_install_input', return_value=True)
    def test_query_install_install(self,  _):
        """ Test query install w/ input """
        self.assertEqual(Package.query_install(), True)

    @patch('util.Package.query_install_input', return_value=False)
    def test_query_install_none(self,  _):
        """ Test query install w/o input """
        self.assertEqual(Package.query_install(), False)

if __name__ == '__main__':
    unittest.main()
