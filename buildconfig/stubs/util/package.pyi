import logging
from pathlib import Path
from typing import Literal

from bs4 import BeautifulSoup
import requests


LOGGER: logging.Logger


class Package(object):

    packages: list = ...

    def __init__(self, li: str, search_term: str) -> None: ...

    @staticmethod
    def get_name_from_lxml(lxml: BeautifulSoup): ...

    @staticmethod
    def get_version_from_lxml(lxml: BeautifulSoup): ...

    @staticmethod
    def get_date_from_lxml(lxml: BeautifulSoup): ...

    @staticmethod
    def get_desc_from_lxml(lxml: BeautifulSoup): ...

    @classmethod
    def list(cls) -> Literal[True]: ...

    @staticmethod
    def name_from_id(id: int) -> str | Literal[False]: ...

    @staticmethod
    def id_from_name(name: str) -> int | Literal[False]: ...

    @staticmethod
    def format_results(soup: BeautifulSoup, package: str) -> bool: ...

    @staticmethod
    def package_info(selector: str | int) -> None: ...

    @staticmethod
    def install_from_id(id: int | None, unittest: bool = ...) -> None: ...

    @staticmethod
    def query_install_input(unittest: bool = ...) -> int: ...

    @staticmethod
    def query_install(unittest: bool) -> bool: ...

    @staticmethod
    def search(package: str, activate_test_case: bool = ...): ...

    @staticmethod
    def request_pypi(package: str) -> requests.Response: ...

    @staticmethod
    def request_pypi_soup(package: str) -> BeautifulSoup: ...

    @staticmethod
    def service_online(url: str = ...) -> bool: ...

    @staticmethod
    def auto_install(root: str = ...) -> list[Path]: ...

    @staticmethod
    def color_path(path: str = ...) -> str: ...

    @staticmethod
    def update_cache(package: str) -> None | Literal[False]: ...

    @staticmethod
    def update_package(package: str) -> None: ...
