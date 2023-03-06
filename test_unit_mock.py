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
from src.util.mock import run_script


class TestMock(unittest.TestCase):
    """ Test that mock util works """

    def test_run_script(self):
        """ Test that run script works """
        run_script() # NOTE there is no physical way to get coverage on a sys.exit call


if __name__ == '__main__':
    unittest.main()
