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
__source__ = 'https://github.com/geowurster/FS_Nav'


# Code for all utilities is based on the same few lines, but with a few small differences
_UtilDefs = {'apps':          'System applications',
             'cyghome':       'User home directory for Cygwin',
             'desktop':       'User desktop',
             'documents':     'User documents',
             'downloads':     'User downloads',
             'dropbox':       'User dropbox',
             'extdrive':      'External volume',
             'gdrive':        'User Google Drive',
             'hd':            'System hard drive',
             'home':          'User home',
             'movies':        'User movies',
             'music':         'User music',
             'pictures':      'User pictures',
             'public':        'User public or on Windows, general public',
             'systembin':     'System bin',
             'userapps':      'User applications',
             'userbin':       'User bin',
             'googledrive':   'User Google Drive',
             'google_drive':  'User Google Drive',
             'mydocuments':   'User documents',
             'my_documents':  'User documents',
             'mymusic':       'User music',
             'my_music':      'User music',
             'mypictures':    'User pictures',
             'my_pictures':   'User pictures',
             'myvideos':      'User videos',
             'my_videos':     'User videos',
             'videos':        'User videos',
             'extvol':        'External volume',
             'extvolume':     'External volume'}
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
__source__ = 'https://github.com/geowurster/FS_Nav'


# Utility specific information
_UtilName = '%s'


def main(args):

    # Instantiate instance of fsnav and configure
    framework = fsnav.UtilFramework(util_args=args, util_name=_UtilName, util_version=__version__,
                                    util_function=fsnav.%s)

    # Execute
    framework.run()


if __name__ == '__main__':
    main(sys.argv[1:])
    exit()'''


def print_help():
    print("""
=== Help Information ===
FS_Nav comes with a set of command line tools, each of which are very similar.
This script builds each from a common bit of code.

By default, all utilities are built, but the user can
          """)
    exit()


def print_usage():
    print("""
Usage: build_utilities.py
  --help             ->  Print help information
  --codes            ->  Print a list of all utility codes
  --skip-util=code   ->  Don't build utility with given code - see help for info
  --keep-util=code   ->  Build utility with given code - see help for info
  --no-extensions    ->  Don't give executables file extension
  --build-dir=path   ->  Where to build the executables
  --permissions=int  ->  Permissions value for executables - defaults to 0777

Advanced options:
  --remove  ->  Removes built utilities - see help for info
  --force   ->  Force a build - see help for info
          """)
    exit()


def print_license():
    print("""
See LICENSE.txt from original distribution
          """)
    exit()


def print_version():
    print("""
build_utilities.py version %s
By %s - %s

Used in the setup and install process for FS_Nav
Source: %s
          """ % (__version__, __author__, __email__, __source__))
    exit()


def print_util_codes():
    print("\n==== Utility Codes ===")
    # Get the longest key
    longest = 0
    for key in _UtilDefs.keys():
        if len(key) > longest:
            longest = len(key)
    for key, val in _UtilDefs.iteritems():
        spaces = ''.join([' ' for i in range(0, longest - len(key))])
        print('  %s' % key + spaces + '  ->  %s' % val)
    print('\n')
    exit()


def main(args):

    # Set defaults
    allowed_utils = _UtilDefs.keys()
    utils_to_build = _UtilDefs.keys()
    keep_utils = []
    drop_utils = []
    build_dir = '..' + sep + 'bin'
    with_extensions = True
    extension = '.py'
    permissions = 0777
    remove_utilities = False
    force_build = False

    # Loop through arguments and configure
    for arg in args:

        # Help arguments
        if arg == '--help':
            print_help()
        elif arg == '--usage':
            print_usage()
        elif arg == '--version':
            print_version()
        elif arg == '--license':
            print_license()
        elif arg == '--codes' or '--code':
            print_util_codes()

        # Filter utilities to build
        elif ('--skip-util=' or '--drop-util=') in arg:
            drop_utils.append(arg.split('=')[1])
        elif '--keep-util=' in arg:
            keep_utils.append(arg.split('=')[1])

        # Change build directory
        elif ('--prefix=' or '--bin-dir=' or '--build-dir=') in arg:
            build_dir = arg.split('=')[1]

        # Additional configurations
        elif ('--no-extensions' or '--no-extension' or '--no-ext') in arg:
            with_extensions = False
        elif ('--extension=' or '-ext=') in arg:
            extension = arg.split('=')[1]
        elif ('--permissions=' or '--perm=') in arg:
                permissions = arg.split('=')[1]
        elif arg == '--clean' or '--remove':
            remove_utilities = True
        elif arg == '--force':
            force_build = True

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
    if len(keep_utils) is not 0:
        utils_to_build = keep_utils
    elif len(drop_utils) is not 0:
        for item in drop_utils:
            try:
                del_index = drop_utils.index(item)
                del utils_to_build[del_index]
            except ValueError:
                print("build_utilities.py ERROR: Can't drop utility: %s" % item)
                exit()

    # Validate
    bail = False
    if not os.path.isdir(build_dir):
        print("build_utilities.py ERROR: Can't find build directory: %s" % build_dir)
        exit()
    try:
        permissions = int(permissions)
    except ValueError:
        print("build_utilities.py ERROR: Invalid permissions - must be an int: %s" % str(permissions))
        bail = True
    for util in utils_to_build:
        if util not in allowed_utils:
            print("build_utilities.py ERROR: Invalid utility code: %s" % util)
            bail = True
    if bail:
        exit()

    # Loop through utilities and build
    for util in utils_to_build:
        if with_extensions:
            util_name = util + extension
            util_path = build_dir + sep + util_name
        else:
            util_name = util + extension
            util_path = build_dir + sep + util_name

        # Remove or build
        if remove_utilities:
            if os.path.isfile(util_path):
                print("Removing " + util_path)
                os.remove(util_path)
            else:
                print("Can't find or remove: %s" % util_path)
        else:
            if os.path.isfile(util_path) and not force_build:
                print("File exists - can't build: %s" % util_path)
            else:
                print("Building " + util_path)
                with open(util_path, 'w') as f:
                    f.write(_UtilCode % (util_name, util_name.split('.')[0]))
                    os.chmod(util_path, permissions)


if __name__ == '__main__':
    main(sys.argv[1:])
    exit()