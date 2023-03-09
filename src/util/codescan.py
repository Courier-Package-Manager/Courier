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

from pathlib import PosixPath
from .update import load_logging_ini
from .package import Package
import logging
import os

load_logging_ini()
logger = logging.getLogger()


class Codescan(object):
    """ Scan for unmet dependencies """
    logger.debug(" 🔎 Searching for compatable files")

    @classmethod
    def scan(cls):
        """ Scan for imports in collected files """

        py_files: list[PosixPath] = Package.auto_install()
        dependencies = []
        folders = []
        keywords = ['src', 'util']

        for file in py_files:
            if os.path.isdir(file): folders.append(file); continue
            with open(str(file.resolve()), 'r') as f:
                for line in f.readlines():
                    if line.startswith('#'): continue
                    if ('import' or ('import' and 'from')) in line:
                        if 'from' not in line:
                            if line.split(' ')[1] not in folders:
                                dependencies.append(line.split(' ')[1])
                                continue
                        dependency = line.split(' ')[1]
                        if dependency.startswith('.'): folders.append(dependency.split('.')[1])
                        if dependency in folders: continue
                        if '.' in dependency:
                            if dependency.split('.')[0] in keywords: continue
                            dependencies.append(dependency.split('.')[0])
                            continue
                        dependencies.append(dependency)
                f.close()
        """
        for dependency in dependencies:
            logger.debug(dependency)
        """
        return dependencies
    
    @classmethod
    def install_dependencies(cls):
        """ Install previous dependencies collected from scan. Scan is run within method. """
        dependencies = cls.scan()
        for dependency in dependencies:
            Package.update_package(dependency)
