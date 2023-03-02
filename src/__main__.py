"""
The MIT License (MIT)

Copyright (c) 2023 Joshua Rose

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
"""

import json

try:
    import requests
except ImportError as exception:
    print("ImportError: module \'requests\' must be externally sourced.", end=" ")
    print("Install file \'requirements.txt\' through pip")
    print("For more information on how to do this, visit https://pip.pypa.io/en/stable/user_guide/")
    raise SystemExit
