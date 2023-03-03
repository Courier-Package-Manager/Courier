# -*- coding=utf-8 -*-
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
import util

logger = logging.getLogger()

if os.path.basename(os.path.normpath(os.getcwd())) != 'Courier':
    logging.info("Doing a testing environment import")
    logging.debug(os.getcwd())
    os.chdir('src')


def main():
    """Currently calling functions for testing"""
    util.loc_package_file()
    logger.debug("Package file {m}update.json{r} was created {d}".format(
        m=colorama.Fore.GREEN,
        r=colorama.Fore.RESET,
        d=util.last_updated()))


util.run_script(__name__, __doc__, main)
