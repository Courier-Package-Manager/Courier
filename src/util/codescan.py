"""
Courier.util.codescan
~~~~~~~~~~~~~~~~~~~~~

Scans python files for unsatisfied imports.

Codescan [verb] (my definition): To scan code for unmet dependencies.
Codescan [noun] (my definition): A report of unmet dependencies.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.

TODO: codescan configuration file
"""

import logging
import os
from pathlib import PosixPath

from .package import Package
from .update import load_logging_ini


class Codescan:
    """Hold methods pertaining to the codescan function"""

    @classmethod
    def scan(cls):
        """Scan for imports in collected files"""

        py_files: list[PosixPath] = Package.auto_install()
        dependencies = []
        folders = []
        keywords = ['src', 'util']

        for file in py_files:
            if os.path.isdir(file):
                folders.append(file)
                continue
            with open(str(file.resolve()), 'r') as f:
                for line in f.readlines():
                    if line.startswith('#'):
                        continue
                    if ('import' or ('import' and 'from')) in line:
                        if 'from' not in line:
                            if line.split(' ')[1] not in folders:
                                dependencies.append(line.split(' ')[1])
                                continue
                        dependency = line.split(' ')[1]
                        if dependency.startswith('.'):
                            folders.append(dependency.split('.')[1])
                        if dependency in folders:
                            continue
                        if '.' in dependency:
                            if dependency.split('.')[0] in keywords:
                                continue
                            dependencies.append(dependency.split('.')[0])
                            continue
                        dependencies.append(dependency)
                f.close()

        return dependencies
    
    @classmethod
    def install_dependencies(cls):
        """Install previous dependencies collected from scan.

        The scan is run within the `install_dependencies` method.
        """

        dependencies = list(set(cls.scan()))
        for dependency in dependencies:
            Package.update_package(dependency)


load_logging_ini()
logger = logging.getLogger()
