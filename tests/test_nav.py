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
            command = ['python', '-B', 'bin' + sep + 'nav.py', code]
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
        sys.path.insert(0, '.')
        reload(fsnav)
        print("TESTING: Imported fnsav from: %s" % fsnav.__file__)
        sys.exit(unittest.main())
    elif fsnav is not None:
        sys.exit(unittest.main())
    else:
        print("ERROR: Couldn't import fsnav")
        sys.exit(1)