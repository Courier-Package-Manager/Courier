import logging

from .package import Package
from .update import load_logging_ini

logger: logging.Logger

class Codescan:
    local_modules: list[str]

    @classmethod
    def scan(cls) -> set[str]: ...
    @classmethod
    def install_dependencies(cls) -> None: ...
