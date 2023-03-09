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

from datetime import datetime as dt
import os
import unittest

from src.util import setup


class TestSetup(unittest.TestCase):
    """ Test constructor file for utils package """

    def test_get_date(self):
        """ Test that date is correct """
        setup.get_date(dt.now(), day=str(1))
        setup.get_date(dt.now(), day=str(2))
        setup.get_date(dt.now(), day=str(3))
        os.system('clear')


if __name__ == '__main__':
    os.system('clear')
    print(f" 🧪 Testing {os.getcwd()}")
    unittest.main()
