import logging

from .codescan import Codescan
from .package import Package
from .setup import get_date
from .update import get_project_folder
from .update import loc_package_file
from .update import last_updated
from .update import scan_dir
from .update import load_logging_ini

__modules__: list[object]
logger: logging.Logger

def display_if_online(url: str) -> bool: ...
