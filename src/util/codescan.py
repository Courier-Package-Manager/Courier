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

Codescan [verb] (my definition): To scan code for unmet dependencies.
Codescan [noun] (my definition): A report of unmet dependencies.

TODO: codescan configuration file
"""
from .update import load_logging_ini
from .package import Package
import logging

load_logging_ini()
logger = logging.getLogger()
logger.level = logging.DEBUG


class Codescan(object):
    """ Scan for unmet dependencies """
    logger.debug(" 🔎 Searching for compatable files")

    @classmethod
    def scan(cls):
        """ Scan for imports in collected files """
        py_files = Package.auto_install()
        for file in py_files:
            with open(file, 'r') as f:
                for line in f.read().strip():
                    if 'import' in f:
                        logger.debug(line)
                f.close()
        return;
