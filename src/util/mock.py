"""
Mocks for testing purposes
As well as generic helper functions
"""
import sys


def run_script(name, main):
    """
    Function as script if invoked as such
    Full credit to https://stackoverflow.com/a/27084447
    """
    if name == '__main__':
        sys.exit(main())
