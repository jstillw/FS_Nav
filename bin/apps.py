import sys
import fsnav


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt'


# Global variables
_ScriptName = sys.argv[0]


# Help functions
def help_info():
    pass


def version_info():
    print(""
          "Usage: %s [--help] [--usage] [--version]"
          "")

def usage_info():
    pass


def license_info():
    pass


def main():

    if fsnav.apps(mode='cd') is not True:
        print("%s ERROR: Could not cd to: %s" % (_ScriptName, str(fsnav.apps(mode='return'))))


if __name__ == '__main__':
    main()
    exit()