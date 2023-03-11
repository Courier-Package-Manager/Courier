import logging

logger: logging.Logger

class Codescan:
    local_modules: list[str]

    @classmethod
    def scan(cls) -> set[str]: ...
    @classmethod
    def install_dependencies(cls) -> None: ...
