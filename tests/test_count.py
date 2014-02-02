#!/usr/bin/env python


import sys
from os import sep
from os import linesep
from glob import glob
import unittest
import subprocess


class TestCount(unittest.TestCase):

    def test_count(self):
        test_items = glob('*') + glob('bin' + sep + '*')
        expected = len(list(set(test_items)))
        # Call count.py and capture result
        command = ['python', '-B', 'bin' + sep + 'count.py', '*', 'bin' + sep + '*']
        count_output = subprocess.Popen(command, stdout=subprocess.PIPE)
        count_output = count_output.stdout.readlines()
        actual = int(count_output[0].replace(linesep, ''))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    sys.exit(unittest.main())