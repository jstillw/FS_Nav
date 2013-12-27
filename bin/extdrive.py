#!/usr/bin/env python


import sys
from sys import exit

sys.path.insert(0, '..')
from src import fsnav

# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt from original package.'


# Utility specific information
_UtilName = 'extdrive.py'


def main(args):

    # Instantiate instance of fsnav and configure
    framework = fsnav.UtilFramework(util_args=args, util_name=_UtilName, util_version=__version__,
                                    util_function=fsnav.extdrive)

    # Execute
    framework.run()


if __name__ == '__main__':
    main(sys.argv[1:])
    exit()