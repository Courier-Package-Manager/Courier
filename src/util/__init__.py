import sys
import socket
import logging

import colorama

from .package import search_for_package  # pyright: ignore
from .package import service_online  # pyright: ignore
from .package import request_pypi  # pyright: ignore
from .package import request_pypi_soup  # pyright: ignore
from .package import service_online  # pyright: ignore
from .package import run_quick_test  # pyright: ignore
from .update import get_project_folder
from .update import loc_package_file
from .update import last_updated
from .update import scan_dir
from .update import update_packages
from .update import load_logging_ini

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
    load_logging_ini,
]

if not service_online():
    logging.critical(" 🌐 https://pypi.org is down")
    sys.exit(1)

# logger.debug(" 🌍 https://pypi.org is up!")

run_quick_test()
