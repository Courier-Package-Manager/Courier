
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
import colorama
from datetime import datetime as dt
from src.util import setup

class TestSetup(unittest.TestCase):
    """ Test constructor file for utils package """

    def test_get_date(self):
        """ Test that date is correct """
        setup.get_date(dt.now(), day=1)
        setup.get_date(dt.now(), day=2)
        setup.get_date(dt.now(), day=3)



if __name__ == '__main__':
    unittest.main()
