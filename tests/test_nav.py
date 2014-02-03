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