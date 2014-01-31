#!/usr/bin/env python


import os
import sys
import getpass
import unittest
from os import sep
from glob import glob
from os.path import expanduser
import fsnav


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt from original package.'
__source__ = 'https://github.com/geowurster/FS_Nav'


# Define platform specific information to improve readability within the tests
if ('darwin' or 'nix') in sys.platform:
    _NormalizedPlatform = 'linux'
    _SystemApps = sep + 'Applications'
    _CygwinHome = None
    _Desktop = os.path.expanduser('~') + sep + 'Desktop'
    _Documents = os.path.expanduser('~') + sep + 'Documents'
    _Downloads = os.path.expanduser('~') + sep + 'Downloads'
    _Dropbox = os.path.expanduser('~') + sep + 'Dropbox'
    _GDrive = os.path.expanduser('~') + sep + 'Google Drive'
    _GitHub = os.path.expanduser('~') + sep + 'GitHub'
    _HD = sep
    _Home = os.path.expanduser('~')
    _Movies = os.path.expanduser('~') + sep + 'Movies'
    _Music = os.path.expanduser('~') + sep + 'Music'
    _Pictures = os.path.expanduser('~') + sep + 'Pictures'
    _Public = os.path.expanduser('~') + sep + 'Public'
    _UserApps = os.path.expanduser('~') + sep + 'Applications'
    _UserBin = os.path.expanduser('~') + sep + 'bin'
    _SystemBin = sep.join(['', 'usr', 'local', 'bin'])
elif 'cygwin' in sys.platform:
    _NormalizedPlatform = 'cygwin'
    _SystemApps = sep.join(['', 'cygdrive', 'c', 'Program Files'])
    _CygwinHome = sep.join(['', 'cygdrive', 'c', 'home', getpass.getuser()])
    _Desktop = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Desktop'])
    _Documents = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Documents'])
    _Downloads = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Downloads'])
    _Dropbox = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Dropbox'])
    _GDrive = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Google Drive'])
    _GitHub = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'GitHub'])
    _HD = sep.join(['', 'cygdrive', 'c'])
    _Home = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Desktop'])
    _Movies = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Videos'])
    _Music = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Music'])
    _Pictures = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Pictures'])
    _Public = sep.join(['', 'cygdrive', 'c', 'Users', 'Public'])
    _UserApps = sep.join(['', 'cygdrive', 'c', 'Program Files'])
    _UserBin = sep.join(['', 'usr', 'local', 'bin'])
    _SystemBin = sep.join(['', 'usr', 'local', 'bin'])
elif 'win' in sys.platform:
    _NormalizedPlatform = 'windows'
    _SystemApps = sep + 'Applications'
    _CygwinHome = sep.join(['', 'cygdrive', 'home'])
    _Desktop = sep.join(['C:', 'Users', getpass.getuser(), 'Desktop'])
    _Documents = sep.join(['C:', 'Users', getpass.getuser(), 'My Documents'])
    _Downloads = sep.join(['C:', 'Users', getpass.getuser(), 'Downloads'])
    _Dropbox = sep.join(['C:', 'Users', getpass.getuser(), 'Dropbox'])
    _GDrive = sep.join(['C:', 'Users', getpass.getuser(), 'Google Drive'])
    _GitHub = os.path.expanduser('~') + sep + 'GitHub'
    _HD = 'C:' + sep
    _Home = sep.join(['C:', 'Users', getpass.getuser()])
    _Movies = sep.join(['C:', 'Users', getpass.getuser(), 'My Videos'])
    _Music = sep.join(['C:', 'Users', getpass.getuser(), 'My Music'])
    _Pictures = sep.join(['C:', 'Users', getpass.getuser(), 'My Pictures'])
    _Public = sep.join(['C:', 'Users', 'Public'])
    _UserApps = sep.join(['C:', 'Users', getpass.getuser(), 'Applications'])
    _UserBin = sep.join(['C:', 'Users', getpass.getuser(), 'Bin'])
    _SystemBin = sep.join(['C:', 'Program Files'])
else:
    print("FS Nav WARNING: Unsupported platform: %s" % sys.platform)
    # Assume the platform is some linux distribution
    _NormalizedPlatform = 'linux'
    _SystemApps = sep + 'Applications'
    _CygwinHome = None
    _Desktop = os.path.expanduser('~') + sep + 'Desktop'
    _Documents = os.path.expanduser('~') + sep + 'Documents'
    _Downloads = os.path.expanduser('~') + sep + 'Downloads'
    _Dropbox = os.path.expanduser('~') + sep + 'Dropbox'
    _GDrive = os.path.expanduser('~') + sep + 'Google Drive'
    _GitHub = os.path.expanduser('~') + sep + 'GitHub'
    _HD = sep
    _Home = os.path.expanduser('~')
    _Movies = os.path.expanduser('~') + sep + 'Movies'
    _Music = os.path.expanduser('~') + sep + 'Music'
    _Pictures = os.path.expanduser('~') + sep + 'Pictures'
    _Public = os.path.expanduser('~') + sep + 'Public'
    _UserApps = os.path.expanduser('~') + sep + 'Applications'
    _UserBin = os.path.expanduser('~') + sep + 'bin'
    _SystemBin = sep.join(['', 'usr', 'local', 'bin'])


# noinspection PyProtectedMember
class TestStandalone(unittest.TestCase):

    def test_try_chdir(self):
        starting_dir = os.getcwd()
        # Test with an existing directory
        extant_dir = os.path.expanduser('~')
        self.assertTrue(fsnav._try_chdir(extant_dir))
        self.assertEqual(extant_dir, os.getcwd())
        os.chdir(starting_dir)
        # Test with a non-existing directory
        non_extant_dir = '__NON_EXISTENT_DIR_DOES_NOT_EXIST__'
        self.assertFalse(fsnav._try_chdir(non_extant_dir))
        self.assertEqual(starting_dir, os.getcwd())


class TestNavigationFunctions(unittest.TestCase):

    def setUp(self):
        self.starting_dir = os.getcwd()
        self.non_extant_dir = '__NON_EXTANT_DIRECTORY__'

    def test_count(self):
        # Test with input values that are all unique
        test_string = expanduser('~') + sep + '*'
        expected = len(list(set(glob(test_string))))
        actual = fsnav.count([test_string])
        self.assertEqual(expected, actual)

    def test_apps(self):
        # Test return mode with an extant directory
        self.assertEqual(_SystemApps, fsnav.apps(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.apps(mode='cd'))
        self.assertEqual(_SystemApps, os.getcwd())

    def test_cyghome(self):
        # Test return mode with an extant directory
        self.assertEqual(_CygwinHome, fsnav.cyghome(mode='return'))
        # Test cd mode with an extant directory
        if _NormalizedPlatform == ('windows' or 'cygwin'):
            self.assertTrue(fsnav.cyghome(mode='cd'))
            self.assertEqual(_CygwinHome, os.getcwd())

    def test_desktop(self):
        # Test return mode with an extant directory
        self.assertEqual(_Desktop, fsnav.desktop(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.desktop(mode='cd'))
        self.assertEqual(_Desktop, os.getcwd())

    def test_documents(self):
        # Test return mode with an extant directory
        self.assertEqual(_Documents, fsnav.documents(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.documents(mode='cd'))
        self.assertEqual(_Documents, os.getcwd())

    def test_downloads(self):
        # Test return mode with an extant directory
        self.assertEqual(_Downloads, fsnav.downloads(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.downloads(mode='cd'))
        self.assertEqual(_Downloads, os.getcwd())

    def test_dropbox(self):
        # Test return mode with an extant directory
        self.assertEqual(_Dropbox, fsnav.dropbox(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.dropbox(mode='cd'))
        self.assertEqual(_Dropbox, os.getcwd())

    def test_gdrive(self):
        # Test return mode with an extant directory
        self.assertEqual(_GDrive, fsnav.gdrive(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.gdrive(mode='cd'))
        self.assertEqual(_GDrive, os.getcwd())

    def test_github(self):
        # Test return mode with an extant directory
        self.assertEqual(_GitHub, fsnav.github(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.github(mode='cd'))
        self.assertEqual(_GitHub, os.getcwd())

    def test_hd(self):
        # Test return mode with an extant directory
        self.assertEqual(_HD, fsnav.hd(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.hd(mode='cd'))
        self.assertEqual(_HD, os.getcwd())

    def test_home(self):
        # Test return mode with an extant directory
        self.assertEqual(_Home, fsnav.home(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.home(mode='cd'))
        self.assertEqual(_Home, os.getcwd())

    def test_movies(self):
        # Test return mode with an extant directory
        self.assertEqual(_Movies, fsnav.movies(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.movies(mode='cd'))
        self.assertEqual(_Movies, os.getcwd())

    def test_music(self):
        # Test return mode with an extant directory
        self.assertEqual(_Music, fsnav.music(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.music(mode='cd'))
        self.assertEqual(_Music, os.getcwd())

    def test_pictures(self):
        # Test return mode with an extant directory
        self.assertEqual(_Pictures, fsnav.pictures(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.pictures(mode='cd'))
        self.assertEqual(_Pictures, os.getcwd())

    def test_public(self):
        # Test return mode with an extant directory
        self.assertEqual(_Public, fsnav.public(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.public(mode='cd'))
        self.assertEqual(_Public, os.getcwd())

    def test_systembin(self):
        # Test return mode with an extant directory
        self.assertEqual(_SystemBin, fsnav.systembin(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.systembin(mode='cd'))
        self.assertEqual(_SystemBin, os.getcwd())

    def test_userapps(self):
        # Test return mode with an extant directory
        self.assertEqual(_UserApps, fsnav.userapps(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.userapps(mode='cd'))
        self.assertEqual(_UserApps, os.getcwd())

    def test_userbin(self):
        # Test return mode with an extant directory
        self.assertEqual(_UserBin, fsnav.userbin(mode='return'))
        # Test cd mode with an extant directory
        self.assertTrue(fsnav.userbin(mode='cd'))
        self.assertEqual(_UserBin, os.getcwd())

    # Test cross platform nomenclature and other increased usability functions
    test_googledrive = test_gdrive
    test_google_drive = test_gdrive
    test_mydocuments = test_documents
    test_my_documents = test_documents
    test_mymusic = test_music
    test_my_music = test_music
    test_mypictures = test_pictures
    test_my_pictures = test_pictures
    test_myvideos = test_movies
    test_my_videos = test_movies
    test_videos = test_movies

    def tearDown(self):
        os.chdir(self.starting_dir)


# Allow tests to be run from the command line in a self-contained script
if __name__ == '__main__':
    sys.exit(unittest.main())