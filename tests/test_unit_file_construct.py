"""
test: tests.test_unit_file_constructor
source: Courier.util.__init__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module tests required dependencies are
initialized and that global references and 
such are set.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

import logging
import os
import unittest

from src.util import display_if_online
from src.util.update import load_logging_ini


class TestUnitFileConstructor(unittest.TestCase):
    """Test unit file constructor"""

    def setUp(self):
        """Set up instances & instance variables"""
        print(f" 🔒 {self.setUp.__doc__}")
        load_logging_ini()
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_display_if_online(self):
        """Test display if online function"""
        print(f" 🌏 {self.test_display_if_online.__doc__}")
        self.assertTrue(display_if_online(url="https://google.com"))
        print(f" 🌍 {self.test_display_if_online.__doc__}")
        display_if_online("https://not_a_website!/lol.com")


if __name__ == "__main__":
    print(f" 🧪 Testing {os.getcwd()}")
    unittest.main()
