"""
source: Courier.util.package
test: tests.test_unit_package_class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module tests the `Package` class
which is used as a part dataclass part
syntax convention to execute both utility
and core methods.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

import logging
import unittest
from src.courier import Courier
from src.util import package

from src.util.package import Package

logger = logging.getLogger()


class TestUnitPackageClass(unittest.TestCase):
    """Test unit package class object"""

    def setUp(self):
        """Set up instances & instance variables"""
        print(f" 📦 {self.setUp.__doc__}")
        self.soup = Package.request_pypi_soup("test")
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_get_name_from_lxml(self):
        """Test get name from lxml"""
        print(f" 🌑 {self.test_get_name_from_lxml.__doc__}")
        Package.get_name_from_lxml(self.soup)

    def test_get_version_from_lxml(self):
        """Test get version from lxml"""
        print(f" 🌘 {self.test_get_version_from_lxml.__doc__}")
        Package.get_version_from_lxml(self.soup)

    def test_get_date_from_lxml(self):
        """Test get date from lxml"""
        print(f" 🌗 {self.test_get_date_from_lxml.__doc__}")
        Package.get_date_from_lxml(self.soup)

    def test_get_desc_from_lxml(self):
        """Get get description from lxml"""
        print(f" 🌖 {self.test_get_desc_from_lxml.__doc__}")
        Package.get_desc_from_lxml(self.soup)

    def test_name_from_id(self):
        """Index packages for name testing each ones id"""
        print(f" 🫀 {self.test_name_from_id.__doc__}")
        Package.search("pygame", True)
        Package.id_from_name(Package.packages[0].name)

    def test_install_from_id(self):
        """Test install from id"""
        print(f" ✴️  {self.test_install_from_id.__doc__}")
        for i in range(-1, 2):
            Package.install_from_id(i, unittest=True)

    def test_id_from_name(self):
        """Index packages for id testing each ones name"""
        print(f" 🌳 {self.test_id_from_name.__doc__}")
        Package.search("pygame", True)
        Package.id_from_name(Package.packages[0].name)

    def test_format_results(self):
        """Test format package search results"""
        print(f" 🐸 {self.test_format_results.__doc__}")
        for package in Package.packages:
            Package.format_results(package, "")

    def test_search(self):
        """Test search for package"""
        print(f" 🌾 {self.test_search.__doc__}")
        Package.search("colorama", True)

    def test_request_pypi_soup(self):
        """Test request pypi soup"""
        print(f" 🌟 {self.__doc__}")
        Package.request_pypi_soup("matplotlib")

    def test_service_online(self):
        """Test service online"""
        print(f" ☂️🌟 {self.test_service_online.__doc__}")
        assert True

    def test_is_installed(self):
        """Test is installed"""
        print(f" 🍉 {self.test_is_installed.__doc__}")
        Package.search("numpy", True)

    def test_get_package_created(self):
        """Test get package created"""
        print(f" 🚸 {self.test_get_package_created.__doc__}")
        courier = Courier()
        courier.get_package_created()
        del courier

    def test_package_list(self):
        """Test package list"""
        print(f"   {self.test_package_list.__doc__}")
        self.assertTrue(Package.list())

    def test_package_args(self):
        """Return package with NULL"""
        print(f"   {self.test_package_args.__doc__}")
        _package = Package(None, "")
        del _package
        _package = Package(None, None)
        del _package
        _package = Package("", None)
        del _package

    def test_package_info(self):
        """Test package info"""
        print(f"   {self.test_package_info.__doc__}")
        with self.assertRaises(ValueError):
            Package.package_info("test")
        with self.assertRaises(ValueError):
            Package.package_info(2)
        with self.assertRaises(ValueError):
            Package.package_info(True)


if __name__ == "__main__":
    unittest.main()
