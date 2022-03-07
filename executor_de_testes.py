#!/usr/bin/env python
# coding: utf-8

import os
import sys
import unittest

ROOT_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    tests = unittest.TestLoader().discover(ROOT_PATH, "*.py")
    result = unittest.TextTestRunner().run(tests)
    if not result.wasSuccessful():
        sys.exit(1)
