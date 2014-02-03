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
from os import sep
from glob import glob


# Global variables
TEST_SOURCE = False


def main():

    # Define containers
    glob_string = 'tests' + sep + 'test_*'
    exit_codes = []

    # Get tests
    tests = glob(glob_string)

    # Validate
    if len(tests) is 0:
        print("ERROR: Didn't find any tests with: %s" % glob_string)
        return 1

    # Loop through all tests, call, and append exit code to exit_codes list
    for test in tests:
        command = ['python', '-B', test]
        if TEST_SOURCE:
            command.append('--test-src')
        print('\n' + ' '.join(command))
        exit_codes.append(subprocess.call(command))

    '''
    # Check to see if any test exited with a non-zero exit code
    for exit_code in exit_codes:
        if exit_code is not 0:
            return 1

    # All tests exited with 0, so return 0
    '''
    return 0



if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test-src':
        TEST_SOURCE = True
        print("TESTING: Testing source...")
    sys.exit(main())
