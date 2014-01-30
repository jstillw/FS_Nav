#!/usr/bin/env python


import os
import sys
from os import sep
from os.path import isdir
from os.path import expanduser


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__license__ = 'See LICENSE.txt from original package.'
__source__ = 'http://github.com/geowurster/FS_Nav'


def main():

    # Cache information
    homedir = expanduser('~')

    # Create directories if they don't already exist
    directories = [sep + 'Applications',
                   homedir + sep + 'Desktop',
                   homedir + sep + 'Documents',
                   homedir + sep + 'Downloads',
                   homedir + sep + 'Dropbox',
                   homedir + sep + 'Google_Drive',
                   homedir + sep + 'GitHub',
                   sep,
                   homedir,
                   homedir + sep + 'Movies',
                   homedir + sep + 'Music',
                   homedir + sep + 'Pictures',
                   homedir + sep + 'Public',
                   homedir + sep + 'Applications',
                   homedir + sep + 'bin',
                   sep.join(['', 'usr', 'local', 'bin'])]
    for directory in directories:
        if not isdir(directory):
            print("Creating directory: %s" % directory)
            os.makedirs(directory)


if __name__ == '__main__':
    sys.exit(main())