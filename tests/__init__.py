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

import os
import sys


os.system('clear')
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "src"
)

print(f" 📸 Adding {SOURCE_PATH} to project path: {PROJECT_PATH}")

UTIL_PATH = os.path.join(
        SOURCE_PATH, 
        "util"
        )

print(f" 📷 Adding {UTIL_PATH} to source path: {SOURCE_PATH}")

sys.path.append(SOURCE_PATH)
sys.path.append(UTIL_PATH)
