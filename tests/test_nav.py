#!/usr/bin/env python


import sys
import subprocess
from os import linesep
from os import sep
import unittest
try:
    import fsnav
except ImportError:
    fsnav = None

# Define globals
TEST_SOURCE = False
UTIL_PATH = 'nav.py'
if 'darwin' in sys.platform:
    _N_PLATFORM = 'mac'
elif 'nix' in sys.platform:
    _N_PLATFORM = 'linux'
elif 'win' in sys.platform:
    _N_PLATFORM = 'win'
elif 'cygwin' in sys.platform:
    _N_PLATFORM = 'cygwin'
else:
    _N_PLATFORM = 'linux'


class TestNav(unittest.TestCase):

    def test_nav(self):
        for code in fsnav.ALIASES.keys():
            # Build a command to test against
            if TEST_SOURCE:
                command = ['python', '-B', UTIL_PATH, '--test-src', code]
            else:
                command = ['python', '-B', UTIL_PATH, code]
            nav_output = subprocess.Popen(command, stdout=subprocess.PIPE)
            actual = nav_output.stdout.readlines()[0].replace(linesep, '')
            # Call fsnav.py function accompanies code
            expected = fsnav.ALIASES[code][0]()
            # Make sure cyghome doesn't cause errors on non-cygwin platforms
            if code == 'cygwin' and _N_PLATFORM == 'cygwin':
                self.assertEqual(expected, actual)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test-src':
        sys.argv.remove('--test-src')
        TEST_SOURCE = True
        UTIL_PATH = 'bin' + sep + 'nav.py'
        print("TESTING: %s" % UTIL_PATH)
        sys.exit(unittest.main())
    else:
        sys.exit(unittest.main())