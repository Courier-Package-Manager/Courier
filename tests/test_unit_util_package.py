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

from requests.exceptions import MissingSchema

from util.package import Package

logger = logging.getLogger()


class TestUtilPackage(unittest.TestCase):
    """ Test util package functions """
    def setUp(self):
        """ Set up instances & instance variables """
        self.package = 'tensorflow'
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_format_results(self):
        """ Test format package search results """
        Package.format_results(Package.packages[0], "")

    def test_search_for_package(self):
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


if __name__ == '__main__':
    unittest.main()
