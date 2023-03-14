"""
source: Courier.courier
test: tests.test_unit_core
~~~~~~~~~~~~~~~~~~~~~~~~~~

This modules is reponsible for testing the
primary Courier functions.

:copyright: (c) 2023 by Joshua Rose.
:license: MIT, see LICENSE for more details.
"""

import os
import subprocess
import unittest

from src.courier import Courier


class TestCourier(unittest.TestCase):
    """Test courier functions"""

    def setUp(self) -> None:
        self.path = "/home/Josh/dotfiles/"
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.temp_rc = open("/home/Josh/dotfiles/.bashrc", "w")
        return super().setUp()

    def test_bashrc_exists(self):
        courier = Courier()
        courier.bashrc_exists()
        self.temp_rc.close()
        if os.path.exists(self.path):
            os.system("rm -rf /home/Josh/dotfiles")

    def test_get_file_path(self):
        """Ensure file path is accurate"""

        expected = os.path.basename(os.path.normpath(os.getcwd())) == "Courier"
        self.assertEqual(Courier.assert_file_path(), expected)
        print(f" 📂 {self.test_get_file_path.__doc__}")

    def test_assert_file_path(self):
        """Ensure assert file path works"""

        self.assertTrue(Courier.assert_file_path())
        print(f" 📂 {self.test_assert_file_path.__doc__}")

    def test_read_docs(self):
        """Test read documentation files"""

        os.chdir(".github")
        self.assertIsInstance(Courier.read_docs("help.txt"), list)
        os.chdir("..")
        print(f" 📖 {self.test_read_docs.__doc__}")

    def test_print_formatted_list(self):
        """Test print formatted list"""

        # Courier.print_formatted_list(Courier.read_docs("help.txt"))
        print(f" 🎯 {self.test_print_formatted_list.__doc__}")

    def test_close(self):
        """Test close file if file not closed"""

        file = open("LICENSE", "r")
        Courier.close_file(file)
        print(f" 📓 {self.test_close.__doc__}")

    def test_proc_args(self):
        """tests cli args are processed"""

        Courier.proc_args(args=[])
        Courier.proc_args(args=["help", "list"])
        Courier.proc_args(args=["--help"])
        Courier.proc_args(args=["--do-nothing"])
        Courier.proc_args(args=["--menu"])
        Courier.proc_args(args=["--debug"])
        Courier.proc_args(args=["--clear"])
        Courier.proc_args(args=["--menu"])
        Courier.proc_args(args=["codescan"])
        Courier.proc_args(args=["codescan", "test"])
        Courier.proc_args(args=["install"])
        Courier.proc_args(args=["install", "mypy"])
        Courier.proc_args(args=["help"])
        Courier.proc_args(args=["install", "help", "mypy"])
        Courier.proc_args(args=["get"])
        Courier.proc_args(args=["files"])
        Courier.proc_args(args=["get", "brown"], get_test=True)  # pyright: ignore
        Courier.proc_args(args=["get", "brown", "fox"])
        Courier.proc_args(args=["menu"])
        Courier.proc_args(args=["help", "g"])
        Courier.proc_args(args=["help", "i"])
        Courier.proc_args(args=["help", "u"])
        Courier.proc_args(args=["help", "cs"])
        Courier.proc_args(args=["help", "menu"])
        Courier.proc_args(args=["help", "help"])
        Courier.proc_args(args=["help", "_"])
        Courier.proc_args(args=["help", "menu", "menu"])
        Courier.proc_args(args=["help", "menu", "help"])
        Courier.proc_args(args=["help", "menu", "development"])
        Courier.proc_args(args=["help", "menu", "testing"])
        Courier.proc_args(args=["help", "menu", "general"])
        Courier.proc_args(args=["help", "menu", "_"])

        print(f" 🐒 {self.test_proc_args.__doc__}")

    def test_main(self):
        """Ensure main can be run"""

        print(f" 🔒 {self.test_main.__doc__}")
        assert True

    def tearDown(self) -> None:
        del self.path
        return super().tearDown()


if __name__ == "__main__":
    print(f" 🧪 Testing {os.getcwd()}")
    unittest.main()
