"""
source: Courier.util.setup
test: tests.test_unit_setup
~~~~~~~~~~~~~~~~~~~~

This module tests utility function(s) that
are used for formatting and general aethetics.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

import unittest
from datetime import datetime as dt
from src.util import setup


class TestSetup(unittest.TestCase):
    """ Test constructor file for utils package """

    def test_get_date(self):
        """ Test that date is correct """
        setup.get_date(dt.now(), day=str(1))
        setup.get_date(dt.now(), day=str(2))
        setup.get_date(dt.now(), day=str(3))


if __name__ == '__main__':
    unittest.main()
