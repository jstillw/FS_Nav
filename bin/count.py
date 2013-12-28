#!/usr/bin/env python


import sys
import fsnav
from sys import exit


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license___ = 'See LICENSE.txt from original distribution'


# Define help functions
def print_usage():
    print('usage')
    exit()


def print_help():
    print('help')
    exit()


def print_version():
    print('version')
    exit()


def print_license():
    print('license')
    exit()


# Actually do stuff
def main(args):

    # Define defaults
    item_list = []

    # Loop through arguments and configure
    for arg in args:

        # Help arguments
        if arg == ('--help' or '-help'):
            print_help()
        elif arg == ('--usage' or '-usage'):
            print_usage()
        elif arg == ('--version' or '-version'):
            print_version()
        elif arg == ('--license' or '-license'):
            print_license()

        # Assume all other arguments are items to glob
        else:
            item_list.append(arg)

    # Call function
    print(fsnav.count(item_list))


# Execute
if __name__ == '__main__':
    main(sys.argv[1:])
    exit()
