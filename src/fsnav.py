import os
import sys
import getpass
from glob import glob
from os import sep


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt'


# Define platform specific information
if ('darwin' or 'nix') in sys.platform:
    _SystemApps = sep + 'Applications'
    _CygwinHome = None
    _Desktop = os.path.expanduser('~') + sep + 'Desktop'
    _Documents = os.path.expanduser('~') + sep + 'Documents'
    _Downloads = os.path.expanduser('~') + sep + 'Downloads'
    _Dropbox = os.path.expanduser('~') + sep + 'Dropbox'
    _GDrive = os.path.expanduser('~') + sep + 'Google_Drive'
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
    _ExtBasePath = sep + 'Volumes'
elif 'cygwin' in sys.platform:
    _SystemApps = sep.join(['', 'cygdrive', 'c', 'Program Files'])
    _CygwinHome = sep.join(['', 'cygdrive', 'c', 'home', getpass.getuser()])
    _Desktop = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Desktop'])
    _Documents = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Documents'])
    _Downloads = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Downloads'])
    _Dropbox = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Dropbox'])
    _GDrive = sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Google_Drive'])
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
    _ExtBasePath = sep + 'cygdrive'
elif 'win' in sys.platform:
    _SystemApps = sep + 'Applications'
    _CygwinHome = sep.join(['', 'cygdrive', 'home'])
    _Desktop = sep.join(['C:', 'Users', getpass.getuser(), 'Desktop'])
    _Documents = sep.join(['C:', 'Users', getpass.getuser(), 'My Documents'])
    _Downloads = sep.join(['C:', 'Users', getpass.getuser(), 'Downloads'])
    _Dropbox = sep.join(['C:', 'Users', getpass.getuser(), 'Dropbox'])
    _GDrive = sep.join(['C:', 'Users', getpass.getuser(), 'Google_Drive'])
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
    _ExtBasePath = ''
else:
    print("FS Nav WARNING: Unsupported platform: %s" % sys.platform)
    # Assume platform is a linux distribution
    _SystemApps = sep + 'Applications'
    _CygwinHome = None
    _Desktop = os.path.expanduser('~') + sep + 'Desktop'
    _Documents = os.path.expanduser('~') + sep + 'Documents'
    _Downloads = os.path.expanduser('~') + sep + 'Downloads'
    _Dropbox = os.path.expanduser('~') + sep + 'Dropbox'
    _GDrive = os.path.expanduser('~') + sep + 'Google_Drive'
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
    _ExtBasePath = sep + 'Volumes'


# Defined as a function to increase readability within each function
def _try_chdir(dir_path):
    try:
        os.chdir(str(dir_path))
        return True
    except OSError:
        return False


# Utility functions
def count(count_items):
    item_list = []
    for item in count_items:
        if os.path.isdir(item):
            item_list += glob(item + sep + '*')
        elif '*' in item:
            item_list += glob(item)
        else:
            item_list.append(item)
    return len(item_list)


# Functions to navigate around the file system
def apps(mode='return'):
    if mode == 'return':
        return _SystemApps
    elif mode == 'cd':
        return _try_chdir(_SystemApps)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def cyghome(mode='return'):
    if mode == 'return':
        return _CygwinHome
    elif mode == 'cd':
        return _try_chdir(_CygwinHome)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def desktop(mode='return'):
    if mode == 'return':
        return _Desktop
    elif mode == 'cd':
        return _try_chdir(_Desktop)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def documents(mode='return'):
    if mode == 'return':
        return _Documents
    elif mode == 'cd':
        return _try_chdir(_Documents)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def downloads(mode='return'):
    if mode == 'return':
        return _Downloads
    elif mode == 'cd':
        return _try_chdir(_Downloads)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def dropbox(mode='return'):
    if mode == 'return':
        return _Dropbox
    elif mode == 'cd':
        return _try_chdir(_Dropbox)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def extdrive(drive_name, mode='return'):
    if mode == 'return':
        return _SystemApps
    elif mode == 'cd':
        if ('darwin' or 'nix') in sys.platform:
            function_return = _try_chdir(_ExtBasePath + sep + drive_name)
        elif 'cygwin' in sys.platform:
            function_return = _try_chdir(_ExtBasePath + sep + drive_name.lower())
        elif 'Windows' in sys.platform:
            function_return = _try_chdir(drive_name.upper() + ':' + sep)
        else:
            function_return = False
            print("%s.%s ERROR: Platform not supported." % (__name__, apps.__name__))
        if function_return is False:
            print("%s.%s ERROR: Can't change to: %s" % (__name__, apps.__name__, drive_name))
            return False
        else:
            return function_return
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def gdrive(mode='return'):
    if mode == 'return':
        return _GDrive
    elif mode == 'cd':
        return _try_chdir(_GDrive)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def github(mode='return'):
    if mode == 'return':
        return _GitHub
    elif mode == 'cd':
        return _try_chdir(_GitHub)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def hd(mode='return'):
    if mode == 'return':
        return _HD
    elif mode == 'cd':
        return _try_chdir(_HD)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def home(mode='return'):
    if mode == 'return':
        return _Home
    elif mode == 'cd':
        return _try_chdir(_Home)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def movies(mode='return'):
    if mode == 'return':
        return _Movies
    elif mode == 'cd':
        return _try_chdir(_Movies)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def music(mode='return'):
    if mode == 'return':
        return _Music
    elif mode == 'cd':
        return _try_chdir(_Music)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def pictures(mode='return'):
    if mode == 'return':
        return _Pictures
    elif mode == 'cd':
        return _try_chdir(_Pictures)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def public(mode='return'):
    if mode == 'return':
        return _Public
    elif mode == 'cd':
        return _try_chdir(_Public)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def systembin(mode='return'):
    if mode == 'return':
        return _SystemBin
    elif mode == 'cd':
        return _try_chdir(_SystemBin)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def userapps(mode='return'):
    if mode == 'return':
        return _UserApps
    elif mode == 'cd':
        return _try_chdir(_UserApps)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


def userbin(mode='return'):
    if mode == 'return':
        return _UserBin
    elif mode == 'cd':
        return _try_chdir(_UserBin)
    else:
        print("%s.%s ERROR: Invalid mode: %s" % (__name__, apps.__name__, mode))
        return False


# Allow for cross platform nomenclature and other increased usability
googledrive = gdrive
google_drive = gdrive
mydocuments = documents
my_documents = documents
mymusic = music
my_music = music
mypictures = pictures
my_pictures = pictures
myvideos = movies
my_videos = movies
videos = movies