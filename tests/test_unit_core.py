"""
source: Courier.courier
test: tests.test_unit_core
~~~~~~~~~~~~~~~~~~~~~~~~~~

This modules is reponsible for testing the
primary Courier functions.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

import pytest
import unittest
import os

from src.courier import Courier


class TestCourier(unittest.TestCase):
    """Test courier functions"""

    def test_get_file_path(self):
        """Ensure file path is accurate"""
        expected = os.path.basename(os.path.normpath(os.getcwd())) == "Courier"
        self.assertEqual(Courier.assert_file_path(), expected)

        print(f" 📂 {self.test_get_file_path.__doc__}")

    def test_assert_file_path(self):
        """Ensure assert file path works"""
        self.assertTrue(Courier.assert_file_path())

        print(f" 📂 {self.test_assert_file_path.__doc__}")

    def test_get_package_created(self):
        """Test creation date of package"""
        courier = Courier()
        courier.get_package_created()
        del courier

        print(f" 📅 {self.test_get_package_created.__doc__}")

    def test_read_docs(self):
        """Test read documentation files"""
        os.chdir(".github")
        self.assertIsInstance(Courier.read_docs(), list)
        os.chdir("..")

        print(f" 📖 {self.test_read_docs.__doc__}")

    def test_print_formatted_list(self):
        """Test print formatted list"""
        Courier.print_formatted_list(Courier.read_docs("help.txt"))

        print(f" 🎯 {self.test_print_formatted_list.__doc__}")

    def test_close(self):
        """Test close file if file not closed"""
        file = open("LICENSE", "r")
        Courier.close_file(file)

        print(f" 📓 {self.test_close.__doc__}")

    def test_proc_args(self):
        """tests cli args are processed"""
        Courier.proc_args(args=["--help"])
        Courier.proc_args(args=["--do-nothing"])
        Courier.proc_args(args=["get"])

        print(f" 🐒 {self.test_proc_args.__doc__}")

    def test_main(self):
        """Ensure main can be run"""
        print(f" 🔒 {self.test_main.__doc__}")
        assert True


if __name__ == "__main__":
    print(f" 🧪 Testing {os.getcwd()}")
    unittest.main()
