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
import unittest

from src.util.update import get_project_folder
from src.util.update import loc_package_file
from src.util.update import last_updated
from src.util.update import scan_dir
from src.util.update import update_packages
from src.util.update import load_logging_ini

logger = logging.getLogger()


class TestUtilPackage(unittest.TestCase):
    """ Test util package functions """
    def setUp(self):
        """ Set up instances & instance variables """
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG


if __name__ == '__main__':
    unittest.main()