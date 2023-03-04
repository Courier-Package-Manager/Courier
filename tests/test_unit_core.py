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

from logging import Logger
import unittest
from src.util import run_script
from src import courier

# TODO test get_file_path() function


class TestCore(unittest.TestCase):

    file_path = courier.get_file_path()

    def test_file_dunder(self):
        run_script(courier.__name__, courier.__doc__, courier.main)

    def test_logger_instance(self):
        self.assertIsInstance(courier.logger, Logger)

    def test_file_path(self):
        if not TestCore.file_path == 'Courier':
            self.assertEqual(courier.get_file_path(), 'Courier')
        else:
            self.assertEqual(courier.get_file_path(), 'src')

    def test_assert_func(self):
        path_is_root = courier.assert_file_path()
        if not path_is_root:
            self.assertEqual(TestCore.file_path, 'Courier')
        else:
            self.assertEqual(TestCore.file_path, 'src')
