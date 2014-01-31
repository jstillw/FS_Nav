#!/usr/bin/env python


import os
import sys
from os import sep


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt from original package'
__source__ = 'https://github.com/geowurster/FS_Nav'


# Define utility codes for assembling functions
_UtilCodes = {'apps':          'System applications',
              'cyghome':       'User home directory for Cygwin',
              'desktop':       'User Desktop',
              'documents':     'User documents',
              'mydocuments':   'User documents',
              'my_documents':  'User documents',
              'downloads':     'User downloads',
              'dropbox':       'User Dropbox',
              'extdrive':      'External volume',
              'extvol':        'External volume',
              'extvolume':     'External volume',
              'gdrive':        'User Google Drive',
              'ghub':          'User GitHub',
              'googledrive':   'User Google Drive',
              'google_drive':  'User Google Drive',
              'hd':            'System hard drive',
              'home':          'User home',
              'movies':        'User movies',
              'myvideos':      'User movies',
              'my_videos':     'User movies',
              'videos':        'User movies',
              'music':         'User music',
              'mymusic':       'User music',
              'my_music':      'User music',
              'pictures':      'User pictures',
              'mypictures':    'User pictures',
              'my_pictures':   'User pictures',
              'public':        'User public or on Windows, general public',
              'systembin':     'System bin',
              'userapps':      'User applications',
              'userbin':       'User bin'}


# Header code for the shell script that creates aliases for all built utilities
_LinuxAliasHeader = """#!/bin/bash

# Build information
__AUTHOR__='Kevin Wurster'
__VERSION__='0.1'
__EMAIL__='wursterk@gmail.com'
__SOURCE__='https://github.com/geowurster/FS_Nav'


# Functions to print out helpful information
PRINT_HELP_INFO() {
    echo "Help info"
    exit
}

PRINT_HELP() {
    echo "Help"
    exit
}

PRINT_VERSION() {
    echo "Version"
    exit
}

PRINT_LICENSE() {
    echo ""
    echo ${__SOURCE__}
    echo ""
    exit
}

# Create aliases
"""


def print_help():
    print("""
=== Help Information ===
FS_Nav comes with a set of command line tools, each of which are very similar.
This script builds each from a common bit of code.

By default, all utilities are built, but the user can
          """)
    return 1


def print_usage():
    print("""
Usage: build_utilities.py
  --help             ->  Print help information
  --codes            ->  Print a list of all utility codes
  --skip-util=code   ->  Don't build utility with given code - see help for info
  --keep-util=code   ->  Build utility with given code - see help for info
  --build-dir=path   ->  Where to build the executables
  --permissions=int  ->  Permissions value for executables - defaults to 0777

Advanced options:
  --clean  ->  Removes built utilities - see help for info
  --force  ->  Force a build - see help for info
          """)
    return 1


def print_license():
    print(__license__)
    return 1


def print_version():
    print("""
build_utilities.py version %s
By %s - %s

Used in the setup and install process for FS_Nav
Source: %s
          """ % (__version__, __author__, __email__, __source__))
    return 1


def print_util_codes():
    print("\n==== Utility Codes ===")
    # Get the longest key
    longest = 0
    for key in _UtilCodes.keys():
        if len(key) > longest:
            longest = len(key)
    for key, val in _UtilCodes.iteritems():
        spaces = ''.join([' ' for i in range(0, longest - len(key))])
        print('  %s' % key + spaces + '  ->  %s' % val)
    print('\n')
    return 1


def main(args):

    # Set defaults
    name_prefix = 'fs_'
    allowed_utils = _UtilCodes.keys()
    utils_to_build = _UtilCodes.keys()
    keep_utils = []
    drop_utils = []
    build_dir = '..' + sep + 'bin'
    with_extensions = True
    extension = '.py'
    permissions = 0777
    remove_utilities = False
    force_build = False
    with_aliases = True
    alias_util_name = 'fsnav_alias_utilities'
    alias_util_ext = ''
    add_extra_codes = False

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
        elif arg == ('--codes' or '--code'):
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
        elif arg == '--no-alias':
            with_aliases = False
        elif '--alias-util-name=' in arg:
            alias_util_name = arg.split('=')[1]
        elif '--alias-util-ext=' in arg:
            alias_util_ext = arg.split('=')[1]
        elif '--name-prefix=' in arg:
            name_prefix = arg.split('=')[1]
        elif ('--no-extensions' or '--no-extension' or '--no-ext') in arg:
            with_extensions = False
        elif ('--extension=' or '--ext=') in arg:
            extension = arg.split('=')[1]
        elif ('--permissions=' or '--perm=') in arg:
            permissions = arg.split('=')[1]
        elif arg == '--clean' or arg == '--remove':
            remove_utilities = True
        elif arg == '--force':
            force_build = True
        elif arg == '--with-extra-codes':
            add_extra_codes = True

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

    # If the alias utility will be built, create the file and write the header
    if with_aliases:
        alias_util_name = alias_util_name + alias_util_ext
        alias_util_path = build_dir + sep + alias_util_name
        if os.path.isfile(alias_util_path) and not force_build:
            print("File exists - can't build: %s" % alias_util_path)
        else:
            print("Building " + alias_util_path)
            with open(alias_util_path, 'w') as f:
                f.write(_LinuxAliasHeader)
                os.chmod(alias_util_path, permissions)

    # Loop through utilities and build
    for util in utils_to_build:
        if with_extensions:
            util_name = name_prefix + util + extension
            util_path = build_dir + sep + util_name
        else:
            util_name = name_prefix + util + extension
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
                    f.write(_UtilCode % (util_name, util))
                    os.chmod(util_path, permissions)
                if with_aliases:
                    with open(alias_util_path, 'a') as f:
                        f.write('function %s() { cd `../bin/nav.py %s` ; }\n' % (util, util))

    # Remove the alias utility if necessary
    if remove_utilities:
        if os.path.isfile(alias_util_path):
            print("Removing " + alias_util_path)
            os.remove(alias_util_path)
        else:
            print("%s ERROR: Can't find or remove: %s" % (sys.argv[0], alias_util_path))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))