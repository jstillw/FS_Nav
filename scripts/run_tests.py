#!/usr/bin/env python

import sys
import glob
import subprocess
from os import sep
from sys import exit


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt'


# Global variables
_TestDir = '..' + sep + 'tests'


def main():

    # Grab all tests and run
    all_tests = glob.glob(_TestDir + sep + '*')
    if len(all_tests) > 0:
        for test in all_tests:
            print("Testing %s" % test)
            subprocess.call(['python', test])
    else:
        print("ERROR: Didn't find any tests in: %s" % _TestDir)
        exit()


if __name__ == '__main__':
    main()
    exit()