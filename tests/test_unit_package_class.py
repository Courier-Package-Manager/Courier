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

logger = logging.getLogger()


class TestUnitPackageClass(unittest.TestCase):
    """ Test unit package class object """
    def setUp(self):
        """ Set up instances & instance variables """
        # self.package = Package()
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_get_name_from_lxml(self):
        """ Test get name from lxml """

    def test_get_version_from_lxml(self):
        """ Test get version from lxml """

    def test_get_date_from_lxml(self):
        """ Test get date from lxml """

    def test_get_desc_from_lxml(self):
        """ Get get description from lxml """

if __name__ == '__main__':
    unittest.main()
