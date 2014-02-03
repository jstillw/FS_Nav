#!/usr/bin/env python


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