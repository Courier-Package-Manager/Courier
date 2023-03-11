"""
source: Courier.courier
test: tests.test_unit_core
~~~~~~~~~~~~~~~~~~~~~~~~~~

This modules is reponsible for testing the
primary Courier functions.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

import unittest
import os

from src.courier import get_package_created
from src.courier import print_formatted_list
from src.courier import assert_file_path
from src.courier import read_docs
from src.courier import main
from src.courier import close_file
from src.courier import proc_args


class TestCourier(unittest.TestCase):
    """ Test courier functions """

    def test_get_file_path(self):
        """ Ensure file path is accurate """
        expected = os.path.basename(os.path.normpath(os.getcwd())) == 'Courier'
        self.assertEqual(assert_file_path(), expected)
        os.system('clear')
        print(f" 📂 {self.__doc__}")

    def test_assert_file_path(self):
        """ Ensure assert file path works """
        self.assertTrue(assert_file_path())
        os.system('clear')
        print(f" 📂 {self.__doc__}")

    def test_get_package_created(self):
        """ Test creation date of package """
        get_package_created()
        os.system('clear')
        print(f" 📅 {self.__doc__}")

    def test_read_docs(self):
        """ Test read documentation files """
        os.chdir('.github')
        self.assertIsInstance(read_docs(), list)
        os.chdir('..')
        os.system('clear')
        print(f" 📖 {self.__doc__}")

    def test_print_formatted_list(self):
        """ Test print formatted list """
        print_formatted_list(read_docs('help.txt'))
        os.system('clear')
        print(f" 🎯 {self.__doc__}")

    def test_close(self):
        """ Test close file if file not closed """
        file = open('LICENSE', 'r')
        close_file(file)
        os.system('clear')
        print(f" 📓 {self.__doc__}")

    def test_proc_args(self):
        """ tests cli args are processed """
        proc_args(args=['--help'])
        proc_args(args=['--do-nothing'])
        proc_args(args=['get'])
        proc_args(args=['get', 'requests'])
        proc_args(args=['file.py', 'requests'])
        proc_args(args=[])
        os.system('clear')
        print(f" 🐒 {self.__doc__}")

    def test_main(self):
        """ Ensure main can be run """
        print(f" 🔒 {self.__doc__}")
        main()


if __name__ == '__main__':
    print(f" 🧪 Testing {os.getcwd()}")
    unittest.main()
