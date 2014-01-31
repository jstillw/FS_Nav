#!/usr/bin/env python


import sys
from sys import exit
import fsnav


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt from original distribution'
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


def print_help():
    print("""
=== Help ===
Packages functionality from all command line utilities into one single tool
First argument must be the utility code assigned to the requested function
All subsequent arguments are funneled into the chosen utility
Use --codes to view a list

Note that the count utility is not accessible via this package
          """)
    exit()


def print_usage():
    print("""
Usage: %s --help-info util_code [utility arguments ...]
          """ % sys.argv[0])
    exit()


def print_version():
    print("""
%s version %s
By %s - %s
          """ % (sys.argv[0], __version__, __author__, __email__))
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


def print_license():
    print('\n' + __license__ + '\n')
    exit()


def print_help_info():
    print("""
=== Help Flags ===
  --help
  --help-info
  --codes
  --usage
  --version
  --license
          """)
    exit()


# Wrap call for testing purposes
def main(args):

    # Look for help arguments first
    for arg in args:

        if arg == '--help-info' or arg == '-help-info' or arg == '--helpinfo' or arg == '-help-info':
            print_help_info()
        elif arg == '--help':
            print_help()
        elif arg == '--usage':
            print_usage()
        elif arg == '--version':
            print_version()
        elif arg == '--codes' or arg == '--code':
            print_util_codes()
        elif arg == '--license':
            print_license()

    # Configure framework based on
    framework = None
    if args[0] == 'apps':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.apps)
    elif args[0] == 'cyghome':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.cyghome)
    elif args[0] == 'desktop':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.desktop)
    elif args[0] == 'documents' or args[0] == 'mydocuments' or args[0] == 'my_documents':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.documents)
    elif args[0] == 'downloads':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.downloads)
    elif args[0] == 'dropbox':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.dropbox)
    elif args[0] == 'extdrive' or args[0] == 'extvol' or args[0] == 'extvolume':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.extdrive)
    elif args[0] == 'gdrive' or args[0] == 'googledrive' or args[0] == 'google_drive':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.gdrive)
    elif args[0] == 'hd':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.hd)
    elif args[0] == 'home':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.home)
    elif args[0] == 'movies' or args[0] == 'videos' or args[0] == 'myvideos' or args[0] == 'my_videos':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.movies)
    elif args[0] == 'music' or args[0] == 'mymusic' or args[0] == 'my_music':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.music)
    elif args[0] == 'pictures' or args[0] == 'mypictures' or args[0] ==  'my_pictures':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.pictures)
    elif args[0] == 'public':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.public)
    elif args[0] == 'systembin':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.systembin)
    elif args[0] == 'userapps':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.userapps)
    elif args[0] == 'userbin':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.userbin)
    else:
        print("%s ERROR: Invalid utility: %s" % (sys.argv[0], args[0]))
        exit()

    # Execute
    framework.run()


# Execute
if __name__ == '__main__':
    main(sys.argv[1:])
    exit()