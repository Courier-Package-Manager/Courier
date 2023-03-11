"""
core: Courier.util.update
test: test_unit_util_update
~~~~~~~~~~~~~~~~~~~~

This modules test Couriers core features as
a program. This module is also responsibile for
testing utility functions and the management of aesthetic
dependencies such as colorama and logging.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

import logging
import os
import unittest

from src.util.update import switch_root
from src.util.update import scan_dir
from src.util.update import create_package
from src.util.update import loc_package_file
from src.util.update import file_exists
from util.package import Package


class TestUtil(unittest.TestCase):
    """ Test util functions """
    def setUp(self):
        """ Set up instances & instance variables """
        print(f" 🦎 {self.setUp.__doc__}")
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_file_exists(self):
        """ Test file exists function works """
        print(f" 🐶 {self.test_file_exists.__doc__}")
        file_exists('non-existent-file', 'r')
        os.system('clear')

    def test_switch_root(self):
        """ Assert that project dir changes """
        print(f" 🍤 {self.test_switch_root.__doc__}")
        os.chdir('src')
        self.assertNotEqual(switch_root(), 'Courier')
        os.system('clear')

    def test_scan_dir(self):
        """ Assert all files are given """
        os.system('clear')
        print(f" 🐈 {self.test_scan_dir.__doc__}")
        scan_dir(files=False)
        os.system('clear')
        print(f" 🐈 {self.test_scan_dir.__doc__}")
        scan_dir(files=True)
        os.system('clear')
        print(f" 🐈 {self.test_scan_dir.__doc__}")
        scan_dir(folders=True)
        os.system('clear')
        print(f" 🐈 {self.test_scan_dir.__doc__}")
        scan_dir(folders=False)
        os.system('clear')

    def test_create_package(self):
        """ Test packages are being created """
        print(f" 🧙 {self.test_create_package.__doc__}")
        create_package()
        os.system('clear')

    def test_update_packages(self):
        """ Test update packages equals return ellipses """
        print(f" 🎾 {self.test_update_packages}")
        for package in Package.packages:
            self.assertIsInstance(Package.update_package(package), bool)
        os.system('clear')

    def test_loc_package_file(self):
        """ Test locate package file """
        os.system('clear')
        print(f" ⛪ {self.test_loc_package_file.__doc__}")
        loc_package_file(debug=True)
        os.system('clear')
        print(f" ⛪ {self.test_loc_package_file.__doc__}")
        loc_package_file(mode='w')
        os.system('clear')
        print(f" ⛪ {self.test_loc_package_file.__doc__}")
        create_package()  # TODO (done) Ensure that package is still reset
        os.system('clear')

if __name__ == '__main__':
    os.system('clear')
    print(f" 🧪 Testing {os.getcwd()}")
    unittest.main()
