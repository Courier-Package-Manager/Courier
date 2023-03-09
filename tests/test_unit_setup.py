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

import os
import unittest
from util import Codescan


class TestCodescan(unittest.TestCase):
    """ Test codescan methods """
    def test_scan(self):
        Codescan.scan()

    def test_install_dependencies(self):
        """ Test install deps from scan """
        Codescan.install_dependencies()


if __name__ == '__main__':
    os.system('clear')
    print(f" 🧪 Testing {os.getcwd()}")
    unittest.main()
