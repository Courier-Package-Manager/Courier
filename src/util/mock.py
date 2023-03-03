"""
Mocks for testing purposes
As well as generic helper functions
"""
import sys


def run_script(name, doc, main):
    """
    Function as script if invoked as such
    Full credit to https://stackoverflow.com/a/27084447
    """
    if name == '__main__':
        if '--help' in sys.argv or '-h' in sys.argv:
            sys.stdout.write(doc)
        else:
            sys.exit(main())
