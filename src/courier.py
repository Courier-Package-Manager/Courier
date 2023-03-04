# -*- coding=utf-8 -*-
# TODO add docstrings to file functions
# TODO relocate file functions
"""
The MIT License (MIT)

Copyright (c) 2023 Joshua Rose

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
"""

import logging
import colorama
import os
from .util import *

logger = logging.getLogger()

def get_file_path() -> str:
    return os.path.basename(os.path.normpath(os.getcwd())) 

def assert_file_path() -> bool:
    os.chdir('src')
    new_file_path = get_file_path()
    logging.debug(new_file_path)
    return new_file_path == 'Courier'

file_path = get_file_path()

if file_path != 'Courier':
    logger.debug(assert_file_path())

def main():
    """Currently calling functions for testing"""
    loc_package_file()
    logger.debug("Package file {m}update.json{r} was created {d}".format(
        m=colorama.Fore.GREEN,
        r=colorama.Fore.RESET,
        d=last_updated()))

run_script(__name__, __doc__, main)
