#!/usr/bin/env python


import sys
import unittest
import subprocess
from os import sep
from sys import exit
from glob import glob
from os import linesep

sys.path.insert(0, '..' + sep)
from src import fsnav


class TestUtilities(unittest.TestCase):

    def test_apps(self):
        util_path = glob('..' + sep + 'bin' + sep + 'apps*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.apps(mode='return'))

    def test_cyghome(self):
        util_path = glob('..' + sep + 'bin' + sep + 'cyghome*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        if util_output == 'None':
            util_output = None
        self.assertEqual(util_output, fsnav.cyghome(mode='return'))

    def test_desktop(self):
        util_path = glob('..' + sep + 'bin' + sep + 'desktop*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.desktop(mode='return'))

    def test_documents(self):
        util_path = glob('..' + sep + 'bin' + sep + 'documents*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.documents(mode='return'))

    def test_downloads(self):
        util_path = glob('..' + sep + 'bin' + sep + 'downloads*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.downloads(mode='return'))

    def test_dropbox(self):
        util_path = glob('..' + sep + 'bin' + sep + 'dropbox*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.dropbox(mode='return'))

    def test_gdrive(self):
        util_path = glob('..' + sep + 'bin' + sep + 'gdrive*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.gdrive(mode='return'))

    def test_hd(self):
        util_path = glob('..' + sep + 'bin' + sep + 'hd*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.hd(mode='return'))

    def test_home(self):
        util_path = glob('..' + sep + 'bin' + sep + 'home*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.home(mode='return'))

    def test_movies(self):
        util_path = glob('..' + sep + 'bin' + sep + 'movies*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.movies(mode='return'))

    def test_music(self):
        util_path = glob('..' + sep + 'bin' + sep + 'music*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.music(mode='return'))

    def test_pictures(self):
        util_path = glob('..' + sep + 'bin' + sep + 'pictures*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.pictures(mode='return'))

    def test_public(self):
        util_path = glob('..' + sep + 'bin' + sep + 'public*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.public(mode='return'))

    def test_systembin(self):
        util_path = glob('..' + sep + 'bin' + sep + 'systembin*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.systembin(mode='return'))

    def test_userapps(self):
        util_path = glob('..' + sep + 'bin' + sep + 'userapps*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.userapps(mode='return'))

    def test_userbin(self):
        util_path = glob('..' + sep + 'bin' + sep + 'userbin*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.userbin(mode='return'))

    def test_googledrive(self):
        util_path = glob('..' + sep + 'bin' + sep + 'googledrive*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.googledrive(mode='return'))

    def test_google_drive(self):
        util_path = glob('..' + sep + 'bin' + sep + 'google_drive*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.google_drive(mode='return'))

    def test_mydocuments(self):
        util_path = glob('..' + sep + 'bin' + sep + 'mydocuments*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.mydocuments(mode='return'))

    def test_my_documents(self):
        util_path = glob('..' + sep + 'bin' + sep + 'my_documents*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.my_documents(mode='return'))

    def test_mymusic(self):
        util_path = glob('..' + sep + 'bin' + sep + 'mymusic*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.mymusic(mode='return'))

    def test_my_music(self):
        util_path = glob('..' + sep + 'bin' + sep + 'my_music*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.my_music(mode='return'))

    def test_mypictures(self):
        util_path = glob('..' + sep + 'bin' + sep + 'mypictures*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.mypictures(mode='return'))

    def test_my_pictures(self):
        util_path = glob('..' + sep + 'bin' + sep + 'my_pictures*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.my_pictures(mode='return'))

    def test_myvideos(self):
        util_path = glob('..' + sep + 'bin' + sep + 'myvideos*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.myvideos(mode='return'))

    def test_my_videos(self):
        util_path = glob('..' + sep + 'bin' + sep + 'my_videos*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.my_videos(mode='return'))

    def test_videos(self):
        util_path = glob('..' + sep + 'bin' + sep + 'videos*')
        # Get utility output information
        util_output = subprocess.Popen(util_path, stdout=subprocess.PIPE)
        util_output = util_output.stdout.readlines()[0].replace(linesep, '')
        self.assertEqual(util_output, fsnav.videos(mode='return'))


if __name__ == '__main__':
    unittest.main()
    exit()