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

import logging
import os
import unittest

from util import display_if_online
from util.package import load_logging_ini


class TestUnitFileConstructor(unittest.TestCase):
    """ Test unit file constructor """
    def setUp(self):
        """ Set up instances & instance variables """
        print(f" 🔒 {self.__doc__}")
        load_logging_ini()
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_display_if_online(self):
        """ Test display if online function """
        print(f" 🌏 {self.__doc__}")
        self.assertTrue(display_if_online(url='https://google.com'))
        os.system('clear')
        print(f" 🌍 {self.__doc__}")
        display_if_online('https://not_a_website!/lol.com')
        os.system('clear')


if __name__ == '__main__':
    os.system('clear')
    print(f" 🧪 Testing {os.getcwd()}")
    unittest.main()
