#!/usr/bin/env python


import os
import sys
from os import sep
from sys import exit


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt from original package'


# Code for all utilities is based on the same few lines, but with a few small differences
_UtilCode = '''#!/usr/bin/env python


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
_UtilName = '%s'


def main(args):

    # Instantiate instance of fsnav and configure
    framework = fsnav.UtilFramework(util_args=args, util_name=_UtilName, util_version=__version__,
                                    util_function=fsnav.apps)

    # Execute
    framework.run()


if __name__ == '__main__':
    main(sys.argv[1:])
    exit()'''


def main(args):

    # Set defaults
    utils_to_build = ['apps', 'cyghome', 'desktop', 'documents', 'downloads',
                      'dropbox', 'extdrive', 'gdrive', 'hd', 'home', 'movies',
                      'music', 'nav', 'pictures', 'public', 'systembin', 'userapps', 'userbin']
    keep_utils = []
    drop_utils = []
    build_dir = '..' + sep + 'bin'
    with_extensions = True
    extension = '.py'

    # Loop through arguments and configure
    for arg in args:

        # Filter utilities to build
        if ('--skip-util=' or '--drop-util=') in arg:
            drop_utils.append(arg.split('=')[1])
        elif '--keep-util=' in arg:
            keep_utils.append(arg.split('=')[1])

        # Change build directory
        elif ('--prefix=' or '--bin-dir=') in arg:
            build_dir = arg.split('=')[1]

        # Additional configurations
        elif ('--no-extensions' or '--no-ext') in arg:
            with_extensions = False
        elif '--extension=' in arg:
            extension = arg.split('=')[1]

        # Catch errors
        elif arg[0] != '-':
            print("build_utilities.py ERROR: Invalid argument before '%s'" % arg)
            exit()
        else:
            print("build_utilities.py ERROR: Invalid argument: %s" % arg)
            exit()

    # Configure utilities to build
    # If user is explicitly specifying which utilities to build, ONLY build those
    # Otherwise, remove utilities if necessary
    if keep_utils is not []:
        utils_to_build = keep_utils
    elif drop_utils is not []:
        for item in drop_utils:
            try:
                del_index = drop_utils.index(item)
            except ValueError:
                print("build_utilities.py ERROR: Can't drop utility: %s" % item)
                exit()
            else:
                del utils_to_build[0]

    # Validate
    bail = False
    if not os.path.isdir(build_dir):
        print("build_utilities.py ERROR: Can't find build directory: %s" % build_dir)
        exit()
    if bail:
        exit()

    # Loop through utilities and build
    print utils_to_build
    for util in utils_to_build:
        print("Building %s" % util)
        if with_extensions:
            util_name = util + extension
            util_path = build_dir + sep + util_name
        else:
            util_name = util + extension
            util_path = build_dir + sep + util_name
        with open(util_path) as f:
            f.write(_UtilCode % util_name)


if __name__ == '__main__':
    main(sys.argv[1:])
    exit()