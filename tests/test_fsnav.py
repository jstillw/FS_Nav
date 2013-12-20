import os
import sys
import getpass
import unittest


# Make sure fsnav.py is being imported from the python package, and not from some site-packages directory
sys.path.insert(0, '..' + os.sep)
from src import fsnav


# Define platform specific information to improve readability within the tests
if ('darwin' or 'nix') in sys.platform:
    _NormalizedPlatform = 'linux'
    _SystemApps = os.sep + 'Applications'
    _CygwinHome = None
    _Desktop = os.path.expanduser('~') + os.sep + 'Desktop'
    _Documents = os.path.expanduser('~') + os.sep + 'Documents'
    _Downloads = os.path.expanduser('~') + os.sep + 'Downloads'
    _Dropbox = os.path.expanduser('~') + os.sep + 'Dropbox'
    _GDrive = os.path.expanduser('~') + os.sep + 'Google_Drive'
    _HD = os.sep
    _Home = os.path.expanduser('~')
    _Movies = os.path.expanduser('~') + os.sep + 'Movies'
    _Music = os.path.expanduser('~') + os.sep + 'Music'
    _Pictures = os.path.expanduser('~') + os.sep + 'Pictures'
    _Public = os.path.expanduser('~') + os.sep + 'Public'
    _UserApps = os.path.expanduser('~') + os.sep + 'Applications'
    _UserBin = os.path.expanduser('~') + os.sep + 'bin'
    _SystemBin = os.sep.join(['', 'usr', 'local', 'bin'])
elif 'cygwin' in sys.platform:
    _NormalizedPlatform = 'cygwin'
    _SystemApps = os.sep + 'Applications'
    _CygwinHome = os.sep.join(['', 'cygdrive', 'home', getpass.getuser()])
    _Desktop = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Desktop'])
    _Documents = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Documents'])
    _Downloads = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Downloads'])
    _Dropbox = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Dropbox'])
    _GDrive = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Google_Drive'])
    _HD = 'C:' + os.sep
    _Home = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Desktop'])
    _Movies = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Movies'])
    _Music = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Music'])
    _Pictures = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Pictures'])
    _Public = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Public'])
    _UserApps = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Applications'])
    _UserBin = os.sep.join(['', 'cygdrive', 'c', 'Users', 'bin'])
    _SystemBin = os.sep.join(['', 'usr', 'local', 'bin'])
elif 'Windows' in sys.platform:
    _NormalizedPlatform = 'windows'
    _SystemApps = os.sep + 'Applications'
    _CygwinHome = os.sep.join(['', 'cygdrive', 'home'])
    _Desktop = os.sep.join(['C:', 'Users', getpass.getuser(), 'Desktop'])
    _Documents = os.sep.join(['C:', 'Users', getpass.getuser(), 'Documents'])
    _Downloads = os.sep.join(['C:', 'Users', getpass.getuser(), 'Downloads'])
    _Dropbox = os.sep.join(['C:', 'Users', getpass.getuser(), 'Dropbox'])
    _GDrive = os.sep.join(['C:', 'Users', getpass.getuser(), 'Google_Drive'])
    _HD = 'C:' + os.sep
    _Home = os.sep.join(['C:', 'Users', getpass.getuser()])
    _Movies = os.sep.join(['C:', 'Users', getpass.getuser(), 'Movies'])
    _Music = os.sep.join(['C:', 'Users', getpass.getuser(), 'Music'])
    _Pictures = os.sep.join(['C:', 'Users', getpass.getuser(), 'Pictures'])
    _Public = os.sep.join(['C:', 'Users', getpass.getuser(), 'Public'])
    _UserApps = os.sep.join(['C:', 'Users', getpass.getuser(), 'Applications'])
    _UserBin = os.sep.join(['C:', 'Users', getpass.getuser(), 'Bin'])
    _SystemBin = os.sep.join(['C:', 'Program Files'])
else:
    print("FS Nav WARNING: Unsupported platform: %s" % sys.platform)
    # Assume the platform is some linux distribution
    _NormalizedPlatform = 'linux'
    _SystemApps = os.sep + 'Applications'
    _CygwinHome = None
    _Desktop = os.path.expanduser('~') + os.sep + 'Desktop'
    _Documents = os.path.expanduser('~') + os.sep + 'Documents'
    _Downloads = os.path.expanduser('~') + os.sep + 'Downloads'
    _Dropbox = os.path.expanduser('~') + os.sep + 'Dropbox'
    _GDrive = os.path.expanduser('~') + os.sep + 'Google_Drive'
    _HD = os.sep
    _Home = os.path.expanduser('~')
    _Movies = os.path.expanduser('~') + os.sep + 'Movies'
    _Music = os.path.expanduser('~') + os.sep + 'Music'
    _Pictures = os.path.expanduser('~') + os.sep + 'Pictures'
    _Public = os.path.expanduser('~') + os.sep + 'Public'
    _UserApps = os.path.expanduser('~') + os.sep + 'Applications'
    _UserBin = os.path.expanduser('~') + os.sep + 'bin'
    _SystemBin = os.sep.join(['', 'usr', 'local', 'bin'])


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

    def tearDown(self):
        os.chdir(self.starting_dir)


if __name__ == '__main__':
    unittest.main()
    exit()