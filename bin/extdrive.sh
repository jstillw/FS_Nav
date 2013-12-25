import sys
import fsnav


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt'


# Global variables
_ScriptName = sys.argv[0]


def main(args):

    if len(args) is not 1:
        print("%s ERROR: N")
    if fsnav.extdrive(mode='cd') is not True:
        print("%s ERROR: Could not cd to: %s" % (_ScriptName, str(fsnav.extdrive(mode='return'))))


if __name__ == '__main__':
    main(sys.argv[1:])
    exit()