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
from os import sep
from os import linesep
from glob import glob
import unittest
import subprocess


# Unless --test-src is used, test whatever is on path
UTIL_PATH = 'count.py'
TEST_SOURCE = False


class TestCount(unittest.TestCase):

    def test_count(self):
        test_items = glob('*') + glob('bin' + sep + '*')
        expected = len(list(set(test_items)))
        # Call count.py and capture result
        if TEST_SOURCE:
            command = ['python', '-B', UTIL_PATH, '--test-src', '*', 'bin' + sep + '*']
        else:
            command = ['python', '-B', UTIL_PATH, '*', 'bin' + sep + '*']
        count_output = subprocess.Popen(command, stdout=subprocess.PIPE)
        count_output = count_output.stdout.readlines()
        # count.py prints a line about testing when --test-src is used, which throws off this test
        # The for loop below finds that line and removes it
        for line in count_output:
            if 'TESTING' in line:
                print(line)
                count_output.remove(line)
        actual = int(count_output[0].replace(linesep, ''))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test-src':
        sys.argv.remove('--test-src')
        TEST_SOURCE = True
        UTIL_PATH = 'bin' + sep + 'count.py'
        print("TESTING: %s" % UTIL_PATH)
        sys.exit(unittest.main())
    else:
        sys.exit(unittest.main())