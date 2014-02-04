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
try:
    import fsnav
except ImportError:
    fsnav = None


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
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
    print(fsnav.__license__)
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

    # If --test-src was given as the first argument, adjust sys.path, reload(fsnav) to test against source code
    if len(sys.argv) > 1 and sys.argv[1] == '--test-src':
        sys.argv.remove('--test-src')
        sys.path.insert(0, '.')
        reload(fsnav)
        print("TESTING: count.py: Imported fsnav from: %s" % fsnav.__file__)
        sys.exit(main(sys.argv[1:]))

    # fnsav was imported - act normally
    elif fsnav is not None:
        if len(sys.argv) is 1:
            sys.argv.append('*')
        sys.exit(main(sys.argv[1:]))

    # fsnav couldn't be imported - exit
    else:
        print("ERROR: Couldn't import fsnav")
        sys.exit(1)