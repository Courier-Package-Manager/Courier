import logging

# TODO import helper, mock, setup & update
from .mock import run_script

from .update import loc_package_file
from .update import get_project_folder
from .update import last_updated
from .update import scan_dir
from .update import update_packages
from .update import load_logging_ini

import colorama

logger = logging.getLogger()

colorama.init()

# NOTE this is to satisfy flake errors, serves no practical
# purpose
__locals__ = [
    get_project_folder,
    loc_package_file,
    last_updated,
    scan_dir,
    update_packages,
    run_script,
    load_logging_ini
]
