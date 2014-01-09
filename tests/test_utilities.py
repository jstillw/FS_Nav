#!/usr/bin/env python


import sys
import unittest
import subprocess
from os import sep
from glob import glob
from os import linesep
try:
    import fsnav
except ImportError:
    fsnav = None


# Build information
__version__ = '0.1'


# Call this function before running any tests to see if tests should be run or not
def validate(verbose=True):
    bail = False
    # Check and see if these tests are designed for the imported version of fsnav
    if __version__ != fsnav.__version__:
        if verbose:
            print("test_utilities.py WARNING: Running test suite against the incorrect version")
            print("  fsnav version = %s" % fsnav.__version__)
            print("  test version  = %s" % __version__)
        bail = True
    if fsnav is None:
        print("test_fsnav.py ERROR: fsnav.py was not successfully imported")
        bail = True
    # Check to see if there is anything to test
    if len(glob('..' + sep + 'bin' + sep + '*')) is 2:
        if verbose:
            print("test_utilities.py ERROR: Run scripts/build_utilities.py before testing")
            print("  Note that this is hard coded to look for 2 utilities that always exist in bin")
        bail = True
    return bail


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


# Allow tests to be run from the command line in a self-contained script
if __name__ == '__main__':

    # Allow this set of tests to be used for two purposes:
    # To test a version that is currently installed
    # To test the src code within a package before it is installed
    if len(sys.argv) > 1:
        if sys.argv[1] == '--test-src':
            del sys.argv[sys.argv.index('--test-src')]
            sys.path.insert(0, '..' + sep + 'src')
            if fsnav is not None:
                r = reload(fsnav)
            else:
                import fsnav

    # Print any warning information about tests using internal validate function
    # This function performs necessary checks
    if validate():
        unittest.main()
    else:
        print("test_utilities.py ERROR: Could not run tests")