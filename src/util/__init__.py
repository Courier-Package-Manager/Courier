import logging
from logging.config import fileConfig

# TODO import helper, mock, setup & update
from .mock import run_script

from .update import loc_package_file
from .update import last_updated
from .update import scan_dir
from .update import update_packages

try:
    import colorama
except ImportError:
    print(" [critical] Install dependencies using makefile.")
    raise SystemExit

fileConfig('config.ini')
logger = logging.getLogger()

colorama.init()

# NOTE this is to simply satisfy flake
__locals__ = [
    loc_package_file,
    last_updated,
    scan_dir,
    update_packages,
    run_script
]
