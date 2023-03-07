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

import unittest
import os
import logging
from src.util.update import switch_root
from src.util.update import scan_dir
from src.util.update import create_package
from src.util.update import update_packages
from src.util.update import loc_package_file
from src.util.update import file_exists
from util import display_if_online


class TestUtil(unittest.TestCase):
    """ Test util functions """
    def setUp(self):
        """ Set up instances & instance variables """
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_file_exists(self):
        """ Test file exists function works """
        file_exists('non-existent-file', 'r')

    def test_switch_root(self):
        """ Assert that project dir changes """
        os.chdir('src')
        self.assertNotEqual(switch_root(), 'Courier')

    def test_scan_dir(self):
        """ Assert all files are given """
        scan_dir(files=False)
        scan_dir(files=True)
        scan_dir(folders=True)
        scan_dir(folders=False)

    def test_create_package(self):
        """ Test packages are being created """
        create_package()

    def test_update_packages(self):
        """ Test update packages equals return ellipses """
        self.assertEqual(update_packages(), Ellipsis)

    def test_loc_package_file(self):
        """ Test locate package file """
        loc_package_file(debug=True)
        loc_package_file(mode='w')
        create_package()  # TODO (done) Ensure that package is still reset

if __name__ == '__main__':
    unittest.main()
