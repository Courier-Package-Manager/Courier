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
import unittest

from util import display_if_online


class TestUnitFileConstructor(unittest.TestCase):
    """ Test unit file constructor """
    def setUp(self):
        """ Set up instances & instance variables """
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_display_if_online(self):
        """ Test display if online function """
        self.assertTrue(display_if_online('https://google.com'))
        self.assertFalse(display_if_online('https://not_a_website!/lol.com'))


if __name__ == '__main__':
    unittest.main()
