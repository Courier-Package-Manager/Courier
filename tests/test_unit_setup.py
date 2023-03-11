"""
source: Courier.util.setup
test: tests.test_unit_setup
~~~~~~~~~~~~~~~~~~~~

This module tests utility function(s) that
are used for formatting and general aethetics.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

import os
import unittest
from src.util import codescan


class TestCodescan(unittest.TestCase):
    """Test codescan methods"""

    def test_scan(self):
        codescan.Codescan.scan()

    def test_install_dependencies(self):
        """Test install deps from scan"""
        codescan.Codescan.install_dependencies()


if __name__ == "__main__":
    print(f" 🧪 Testing {os.getcwd()}")
    unittest.main()
