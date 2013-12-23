#!/usr/bin/env python


import os
import sys
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
        # Test with just a path to a directory
        directory = '..' + sep + 'src'
        self.assertEqual(len(glob(directory + sep + '*')), fsnav.count(directory, mode=''))
        # Test with just a path to a directory and a wildcard
        directory = '..' + sep + 'src'
        file_list = glob('*')
        submission_list = directory + file_list  # Give the method a single list
        self.assertEqual(len(glob(directory + sep + '*') + file_list), fsnav.count(submission_list))
        # Test with just a path to a directory, random files, and a string containing a wildcard


    def tearDown(self):
        os.chdir(self.current_dir)



# Execute
if __name__ == '__main__':
    unittest.main()
    exit()