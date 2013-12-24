#!/usr/bin/env python


import os
import sys
import site
from sys import exit
from glob import glob
from os.path import sep


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt'


def print_help():
    pass


def print_usage():
    pass


def print_version():
    pass


def main(args):

    # Define defaults
    src_code = 'src' + sep + 'fsnav.py'
    utilities = [i for i in glob('src' + sep + '*') if '__init__' not in i]  # init file is for testing only
    site_packages = site.getsitepackages()[0]



if __name__ == '__main__':
    main(sys.argv)