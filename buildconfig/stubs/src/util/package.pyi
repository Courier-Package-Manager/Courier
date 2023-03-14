from .setup import escape_ansi as escape_ansi
from .update import load_logging_ini as load_logging_ini
from _typeshed import Incomplete
from bs4 import BeautifulSoup
from typing import List

class Package:
    packages: List
    name: Incomplete
    version: Incomplete
    date: Incomplete
    description: Incomplete
    id: Incomplete
    def __init__(self, li, search_term) -> None: ...
    @staticmethod
    def get_name_from_lxml(lxml): ...
    @staticmethod
    def get_version_from_lxml(lxml: BeautifulSoup): ...
    @staticmethod
    def get_date_from_lxml(lxml: BeautifulSoup): ...
    @staticmethod
    def get_desc_from_lxml(lxml): ...
    @classmethod
    def list(cls): ...
    @staticmethod
    def name_from_id(id): ...
    @staticmethod
    def id_from_name(name): ...
    @staticmethod
    def format_results(soup, package): ...
    @staticmethod
    def package_info(selector) -> None: ...
    @staticmethod
    def install_from_id(id, unittest) -> None: ...
    @staticmethod
    def query_install_input(unittest): ...
    @staticmethod
    def handle_query_input(selected, unittest): ...
    @staticmethod
    def query_install(unittest): ...
    @staticmethod
    def search(package, unittest: bool = ...): ...
    @staticmethod
    def request_pypi(package): ...
    @staticmethod
    def request_pypi_soup(package): ...
    @staticmethod
    def service_online(url: str = ...): ...
    @staticmethod
    def auto_install(root: str = ...): ...
    @staticmethod
    def color_path(path=...): ...
    @staticmethod
    def update_cache(package): ...
    @staticmethod
    def update_package(package) -> None: ...

LOGGER: Incomplete
