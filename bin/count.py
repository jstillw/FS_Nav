#!/usr/bin/env python


import sys
import fsnav
from sys import exit


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt from original distribution'
__source__ = 'https://github.com/geowurster/FS_Nav'


# Define help functions
def print_usage():
    print("""
Usage: %s --help-info dir|file|wildcard
          """)
    return 1


def print_help():
    print("""
=== Help ===
Simple utility for counting files and directories
Running without any arguments counts everything in the current directory
Giving a directory will count the contents within that directory
Directories, files, and wildcards can be mixed and matched

Example:
count.py /path/to/directory /path/to/individual/file.ext /path/to/something/*
          """)
    return 1


def print_version():
    print("""
%s version %s

By %s - %s
          """ % (sys.argv[0], __version__, __author__, __email__))
    return 1


def print_license():
    print('\n' + __license__ + '\n')
    return 1


def print_help_info():
    print("""
=== Help Flags ===
  --help
  --help-info
  --usage
  --version
  --license
          """)
    return 1


# Actually do stuff
def main(args):

    # Define defaults
    item_list = []

    # Loop through arguments and configure
    for arg in args:

        # Help arguments
        if arg == ('--help-info' or '-helpinfo' or '-help-info' or '--helpinfo'):
            return print_help_info()
        elif arg == ('--help' or '-help'):
            return print_help()
        elif arg == ('--usage' or '-usage'):
            return print_usage()
        elif arg == ('--version' or '-version'):
            return print_version()
        elif arg == ('--license' or '-license'):
            return print_license()

        # Assume all other arguments are items to glob
        else:
            item_list.append(arg)

    # Call function
    print(fsnav.count(item_list))
    return 0


# Execute
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
