#!/usr/bin/env python


import os
import unittest
from os import sep
from sys import exit
from glob import glob


# Make sure count.py is being imported from the python package, and not from some site-packages directory
sys.path.insert(0, '..' + sep)
from bin import count


class TestMain(unittest.TestCase):

    def setUp(self):
        self.current_dir = os.getcwd()

    def test_main(self):
        # Get some files to compare to
        just_directory =
        just_directory_contents = '..' + sep + 'src' + sep + '*'

    def tearDown(self):
        os.chdir(self.current_dir)



# Execute
if __name__ == '__main__':
    unittest.main()
    exit()