#!/usr/bin/env python


import sys
import fsnav
from sys import exit


# Build information
__author__ = fsnav.__author__
__version__ = '0.1'
__email__ = fsnav.__email__
__license___ = fsnav.__license__


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

    # Define constraints
    allowed_modes = ['print', 'return']

    # Define defaults
    item_list = []
    mode = 'print'

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

    # Validate
    bail = False
    if mode not in allowed_modes:
        print("count.py ERROR: Invalid mode: %s" % mode)
        print("  Allowed modes = %s" % ' '.join(allowed_modes))
    if bail:
        exit()

    # Call function
    function_result = fsnav.count(item_list)
    if mode == 'print':
        print(function_result)
    elif mode == 'return':
        return function_result
    else:
        print("count.py ERROR: Bad mode that should have been caught by the validation step.  Oops...")
        exit()


# Execute
if __name__ == '__main__':
    main(sys.argv[1:])
    exit()
