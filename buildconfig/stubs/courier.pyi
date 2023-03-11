from io import TextIOWrapper
import pathlib
from typing import Literal

class Courier(object):
    def __init__(self) -> None: ...
    def get_bashrc_created(self) -> None: ...
    def add_bashrc_alias(self) -> None: ...
    @staticmethod
    def close_file(file: TextIOWrapper) -> None: ...
    @staticmethod
    def get_file_path() -> str: ...
    @staticmethod
    def assert_file_path() -> bool: ...
    @staticmethod
    def read_docs(file: str) -> bool: ...
    @staticmethod
    def print_formatted_list(lines: list[str]) -> None: ...
    @staticmethod
    def proc_args(args: list[str]) -> None: ...
    @staticmethod
    def bashrc_exists() -> pathlib.Path | Literal[False]: ...
