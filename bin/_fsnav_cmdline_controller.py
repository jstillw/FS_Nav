#!/usr/bin/env python


import sys
import fsnav
from sys import exit


# Build information
__author__ = fsnav.__author__
__version__ = '0.1'
__email__ = fsnav.__email__
__license__ = fsnav.__license__


# Wrap call for testing purposes
def main(args):

    # Configure framework based
    if args[0] == 'apps':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.apps)
    elif args[0] == 'cyghome':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.cyghome)
    elif args[0] == 'desktop':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.desktop)
    elif args[0] == 'documents':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.documents)
    elif args[0] == 'downloads':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.downloads)
    elif args[0] == 'dropbox':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.dropbox)
    elif args[0] == 'extdrive':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.extdrive)
    elif args[0] == 'gdrive':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.gdrive)
    elif args[0] == 'hd':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.hd)
    elif args[0] == 'home':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.home)
    elif args[0] == 'movies':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.movies)
    elif args[0] == 'music':
        framework = fsnav.UtilFramework(util_args=args[1:], util_version=__version__,
                                        util_name=args[0], util_function=fsnav.music)
    elif args[0] == 'pictures':
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