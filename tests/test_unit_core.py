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
from src.courier import get_file_path, get_package_created
from src.courier import assert_file_path
from src.courier import loc_package_file
from src.courier import last_updated
from src.courier import run_script
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

    def test_main(self):
        """ Ensure main can be run """
        main()


if __name__ == '__main__':
    unittest.main()
