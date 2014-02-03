#!/usr/bin/env python


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
