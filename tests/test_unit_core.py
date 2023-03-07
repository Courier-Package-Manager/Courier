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
from src.courier import close, get_file_path, proc_args
from src.courier import get_package_created
from src.courier import print_formatted_list
from src.courier import assert_file_path
from src.courier import read_docs
from src.courier import main


class TestCourier(unittest.TestCase):
    """ Test courier functions """
    def test_get_file_path(self):
        """ Ensure file path is accurate """
        expected = os.path.basename(os.path.normpath(os.getcwd()))
        self.assertEqual(get_file_path(), expected)

    def test_assert_file_path(self):
        """ Ensure assert file path works """
        self.assertTrue(assert_file_path())

    def test_get_package_created(self):
        """ Test creation date of package """
        get_package_created()

    def test_read_docs(self):
        """ Test read docuentation files """
        os.chdir('build')
        self.assertIsInstance(read_docs(), list)
        os.chdir('..')

    def test_print_formatted_list(self):
        """ Test print formatted list """
        print_formatted_list(read_docs('help.txt'))

    def test_close(self):
        """ Test close file if file not closed """
        file = open('LICENSE', 'r')
        close(file)

    def test_proc_args(self):
        """ tests cli args are processed """
        proc_args(args=['--help'])
        proc_args(args=['--do-nothing'])
        proc_args(args=['get'])
        proc_args(args=['get', 'requests'])
        proc_args(args=[])

    def test_main(self):
        """ Ensure main can be run """
        main()


if __name__ == '__main__':
    unittest.main()
