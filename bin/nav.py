#!/usr/bin/env python


# =================================================================================== #
#
# New BSD License
#
# Copyright (c) 2014, Kevin D. Wurster
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * The names of its contributors may not be used to endorse or promote products
#   derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# =================================================================================== #


import sys
import fsnav


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__source__ = 'https://github.com/geowurster/FS_Nav'


def print_help():
    print("""
=== Help ===
A utility for exposing FS_Nav's navigation functions via the command line
for scripting purposes.  FS_Nav also comes with fsnav_generator.sh, which
when called as "source fsnav_generator.sh", will generate a set of functions
to make command line navigation easier.  Calling "nav.py link" will
print the command necessary to generate the functions.  Incorporate this
call into your bash profile to generate functions on startup.

Example:
Calling "nav.py desktop" will print the path to the user's desktop
Calling "cd `nav.py desktop`" will cd to the user's desktop

Generating functions via "source fsnav_generator.sh"
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


def print_codes():
    # Print header
    print("")
    print("== Codes/Functions ==")
    # Get keys listed in alphabetical order
    codes = sorted(fsnav.ALIASES.keys())
    for code in codes:
        help_text = fsnav.ALIASES[code][1]
        aliases = str(fsnav.ALIASES[code][2:]).replace('[', '').replace(']', '')
        print("  %s: %s" % (help_text, aliases))
    print("")
    return 1


def print_license():
    print(fsnav.__license__)
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
    generator = 'fsnav_generator.sh'
    source = 'source'
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
        elif arg in ['--codes', '--code', '--functions', '--function']:
            return print_codes()
        elif arg in ['--license', '-usage']:
            return print_license()
        elif '--generator=' in arg or '-generator=' in arg:
            generator = arg.split('=')[1]
        elif '--source=' in arg or '-source=' in arg:
            source = arg.split('=')[1]
        else:
            code = arg

    # Validate
    if code is None:
        print("ERROR: No code supplied")
        return 1

    # Print linking command
    elif code in ['generator', 'generate']:
        print(source + ' ' + generator)
        return 0
    elif code == 'profile':
        print("# Add FS_Nav function generation on startup")
        print("if [ '`which nav.py`' != '' ] && [ '`which %s`' != '' ]; then" % generator)
        print("    %s %s" % (source, generator))
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
    elif sys.argv > 1 and sys.argv[1] == '--test-src':
        sys.argv.remove('--test-src')
        sys.path.insert(0, '.')
        reload(fsnav)
        print("TESTING: nav.py: Imported fsnav from: %s" % fsnav.__file__)
        sys.exit(main(sys.argv[1:]))

    # fsnav was imported - act normally
    elif fsnav is not None:
        sys.exit(main(sys.argv[1:]))

    # fsnav couldn't be imported - exit
    else:
        print("ERROR: Couldn't import fsnav")
        sys.exit(1)