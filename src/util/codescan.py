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
import pathlib

import pkg_resources
from .package import Package
from .update import load_logging_ini


class Codescan:
    """Hold methods pertaining to the codescan function"""

    local_modules = [d.project_name for d in pkg_resources.working_set]
    local_modules.remove('util')

    @classmethod
    def scan(cls):
        """Scan for imports in collected files"""

        py_files: list[PosixPath] = Package.auto_install()
        dependencies = set()
        folders = [i.name for i in pathlib.Path('.').rglob('*') if i.is_dir()]

        for file in py_files:
            if not os.path.isdir(file):
                with open(str(file.resolve()), 'r') as f:
                    for line in f.readlines():
                        if not line.startswith('#'):
                            if ('import' or ('import' and 'from')) in line:
                                if 'from' not in line.split(' '):
                                    if line.split(' ')[1] not in folders:
                                        dependencies.add(line.split(' ')[1])
                                dependency = line.split(' ')[1]
                                dependencies.add(dependency)
                    f.close()

        return dependencies
    
    @classmethod
    def install_dependencies(cls):
        """Install previous dependencies collected from scan.

        The scan is run within the `install_dependencies` method.
        """

        dependencies = cls.scan()
        for dependency in dependencies:
            if dependency in Codescan.local_modules:
                Package.update_package(dependency)

load_logging_ini()
logger = logging.getLogger()
