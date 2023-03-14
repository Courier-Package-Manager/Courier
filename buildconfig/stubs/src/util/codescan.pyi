from .package import Package as Package
from .update import load_logging_ini as load_logging_ini
from _typeshed import Incomplete

class Codescan:
    local_modules: Incomplete
    @classmethod
    def scan(cls): ...
    @classmethod
    def install_dependencies(cls) -> None: ...

logger: Incomplete
