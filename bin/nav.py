#!/usr/bin/env python


import sys
import fsnav


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt from original distribution'
__source__ = 'https://github.com/geowurster/FS_Nav'


def print_help():
    print("""
=== Help ===
A utility for exposing FS_Nav's navigation functions via the command line
for scripting purposes.  FS_Nav also comes with fsnav_linker.sh, which
when called as "source fsnav_linker.sh", will generate a set of functions
to make command line navigation easier.  Calling "nav.py link" will
print the command necessary to generate the functions.  Incorporate this
call into your bash profile to generate functions on startup.

Example:
Calling "nav.py desktop" will print the path to the user's desktop
Calling "cd `nav.py desktop`" will cd to the user's desktop

Generating functions via "source fsnav_linker.sh"
and then calling "desktop" will cd to the user's desktop without
having to call "cd `nav.py desktop`"

A list of codes and their explanation can be viewed with the --codes argument.
          """)
    return 1


def print_usage():
    print("""
Usage: nav.py --help-info code
          """)
    return 1


def print_version():
    print("""
FS_Nav version %s
nav.py version %s
By %s - %s
          """ % (fsnav.__version__, __version__, __author__, __email__))
    return 1


def print_util_codes():
    # Get keys listed in alphabetical order
    codes = sorted(fsnav.ALIASES.iteritems())
    for code in codes:
        help_text = fsnav.ALIASES[code][1]
        aliases = fsnav.ALIASES[code][2:].replace('[', '').replace(']', '')
        print("  %s: %s" % (help_text, aliases))
    return 1


def print_license():
    print('\n' + __license__ + '\n')
    return 1


def print_help_info():
    print("""
The following flags print help information:
  --help-info
  --version
  --license
  --codes
  --usage
  --help
          """)
    return 1


# Wrap call for testing purposes
def main(args):

    # Defaults
    linker = 'fsnav_linker.sh'
    code = None

    # Look for help arguments first
    for arg in args:

        if arg in ['--help-info', '-help-info', '--helpinfo', '-help-info']:
            return print_help_info()
        elif arg in ['--help', '-help']:
            return print_help()
        elif arg in ['--usage', '-usage']:
            return print_usage()
        elif arg in ['--version', '-version']:
            return print_version()
        elif arg in ['--codes', '--code']:
            return print_util_codes()
        elif arg in ['--license', '-usage']:
            return print_license()
        elif '--linker=' in arg or '-linker=' in arg:
            linker = arg.split('=')[1]
        else:
            code = arg

    # Validate
    if code is None:
        print("ERROR: No code supplied")
        return 1

    # Print linking command
    elif code == 'linker':
        print(linker)
        return 0
    elif code == 'link':
        print("source %s" % linker)
        return 0
    elif code == 'profile':
        print("# Add FS_Nav function generation on startup")
        print("if [ '`which nav.py`' != '' ] && [ '`which fsnav_linker.sh`' != '' ]; then")
        print("    source %s" % linker)
        print("fi")
        return 0

    # Print directory path based on code
    elif code in fsnav.ALIASES[code][2:]:
        print(fsnav.ALIASES[code][0]())
        return 0
    else:
        print("ERROR: Invalid code: %s" % code)
        return 1


# Execute
if __name__ == '__main__':
    # If no arguments, print usage and exit
    if len(sys.argv) is 1:
        sys.exit(print_usage())

    # If --test-src was given as the first argument, adjust sys.path, reload(fsnav) to test against source code
    if sys.argv > 1 and sys.argv[1] == '--test-src':
        sys.argv.remove('--test-src')
        sys.path.insert(0, '.')
        reload(fsnav)
        print("TESTING: count.py: Imported fsnav from: %s" % fsnav.__file__)
        sys.exit(main(sys.argv[1:]))

    # fsnav was imported - act normally
    elif fsnav is not None:
        sys.exit(main(sys.argv[1:]))

    # fsnav couldn't be imported - exit
    else:
        print("ERROR: Couldn't import fsnav")
        sys.exit(1)