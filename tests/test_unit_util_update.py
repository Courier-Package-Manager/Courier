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

from src.util import update
from src.util.update import switch_root
from src.util.update import create_package
from src.util.update import loc_package_file
from src.util.update import file_exists


class TestUtil(unittest.TestCase):
    """Test util functions"""

    def setUp(self):
        """Set up instances & instance variables"""
        print(f" 🦎 {self.setUp.__doc__}")
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_file_exists(self):
        """Test file exists function works"""
        print(f" 🐶 {self.test_file_exists.__doc__}")
        file_exists("non-existent-file", "r")

    def test_switch_root(self):
        """Assert that project dir changes"""
        print(f" 🍤 {self.test_switch_root.__doc__}")
        os.chdir("src")
        self.assertNotEqual(switch_root(), "Courier")

    def test_scan_dir(self):
        """Assert all files are given"""

        print(f" 🐈 {self.test_scan_dir.__doc__}")
        update.scan_dir(files=False)

        print(f" 🐈 {self.test_scan_dir.__doc__}")
        update.scan_dir(files=True)

        print(f" 🐈 {self.test_scan_dir.__doc__}")
        update.scan_dir(folders=True)

        print(f" 🐈 {self.test_scan_dir.__doc__}")
        update.scan_dir(folders=False)

    def test_create_package(self):
        """Test packages are being created"""
        print(f" 🧙 {self.test_create_package.__doc__}")
        create_package()

    def test_loc_package_file(self):
        """Test locate package file"""

        print(f" ⛪ {self.test_loc_package_file.__doc__}")
        loc_package_file(debug=True)

        print(f" ⛪ {self.test_loc_package_file.__doc__}")
        loc_package_file(mode="w")

        print(f" ⛪ {self.test_loc_package_file.__doc__}")
        create_package()  # TODO (done) Ensure that package is still reset


if __name__ == "__main__":
    print(f" 🧪 Testing {os.getcwd()}")
    unittest.main()
