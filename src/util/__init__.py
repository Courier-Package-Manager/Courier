import logging
from typing import Type

import colorama
from requests.models import MissingSchema

from .package import Package  # pyright: ignore
from .update import get_project_folder
from .update import loc_package_file
from .update import last_updated
from .update import scan_dir
from .update import update_packages
from .update import load_logging_ini

logger = logging.getLogger()

colorama.init()

# NOTE this is to satisfy flake errors, serves no practical purpose
__locals__ = [
    get_project_folder,
    loc_package_file,
    last_updated,
    scan_dir,
    update_packages,
    load_logging_ini,
]


def display_if_online(url) -> bool | Type[MissingSchema] | None:
    """ Display if pypi is online """
    try:
        if Package.service_online(url):
            logger.debug(f" 🌍 {url} is up!")
            return True
    except MissingSchema:
        raise MissingSchema
    except Exception:
        return False

"""
if not service_online():
    logging.critical(" 🌐 https://pypi.org is down")
    sys.exit(1)
"""
# logger.debug(" 🌍 https://pypi.org is up!")

