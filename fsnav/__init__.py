import os
import sys
import getpass
from os import sep
from glob import glob

# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt from original package.'
__source__ = 'https://github.com/geowurster/FS_Nav'


# Global variables
HOMEDIR = os.path.expanduser('~')
USERNAME = getpass.getuser()
UTIL_CODES = ['apps', 'desktop', 'documents', 'downloads',
              'hd', 'home', 'movies', 'music', 'pictures', 'public',
              'systembin', 'extdrive', 'dropbox', 'gdrive',
              'github', 'userbin', 'user_apps', 'cyghome']
N_PLAT_WARN = False
if 'darwin' in sys.platform:
    N_PLATFORM = 'mac'
    UTIL_CODES.remove('cyghome')
elif 'nix' in sys.platform:
    N_PLATFORM = 'linux'
    UTIL_CODES.remove('cyghome')
elif 'win' in sys.platform:
    N_PLATFORM = 'win'
    UTIL_CODES.remove('cyghome')
elif 'cygwin' in sys.platform:
    N_PLATFORM = 'cygwin'
else:
    N_PLAT_WARN = True
    N_PLATFORM = 'linux'


# Define platform specific information
if N_PLATFORM == 'linux' or N_PLATFORM == 'mac':
    _SystemApps = sep + 'Applications'
    _CygwinHome = None
    _Desktop = HOMEDIR + sep + 'Desktop'
    _Documents = HOMEDIR + sep + 'Documents'
    _Downloads = HOMEDIR + sep + 'Downloads'
    _Dropbox = HOMEDIR + sep + 'Dropbox'
    _GDrive = HOMEDIR + sep + 'Google Drive'
    _GitHub = HOMEDIR + sep + 'GitHub'
    _HD = sep
    _Home = HOMEDIR
    _Movies = HOMEDIR + sep + 'Movies'
    _Music = HOMEDIR + sep + 'Music'
    _Pictures = HOMEDIR + sep + 'Pictures'
    _Public = HOMEDIR + sep + 'Public'
    _UserApps = HOMEDIR + sep + 'Applications'
    _UserBin = HOMEDIR + sep + 'bin'
    _SystemBin = sep.join(['', 'usr', 'local', 'bin'])
    _ExtBasePath = sep + 'Volumes'
elif N_PLATFORM == 'cygwin':
    _SystemApps = sep.join(['', 'cygdrive', 'c', 'Program Files'])
    _CygwinHome = sep.join(['', 'cygdrive', 'c', 'home', USERNAME])
    _Desktop = sep.join(['', 'cygdrive', 'c', 'Users', USERNAME, 'Desktop'])
    _Documents = sep.join(['', 'cygdrive', 'c', 'Users', USERNAME, 'Documents'])
    _Downloads = sep.join(['', 'cygdrive', 'c', 'Users', USERNAME, 'Downloads'])
    _Dropbox = sep.join(['', 'cygdrive', 'c', 'Users', USERNAME, 'Dropbox'])
    _GDrive = sep.join(['', 'cygdrive', 'c', 'Users', USERNAME, 'Google Drive'])
    _GitHub = sep.join(['', 'cygdrive', 'c', 'Users', USERNAME, 'GitHub'])
    _HD = sep.join(['', 'cygdrive', 'c'])
    _Home = sep.join(['', 'cygdrive', 'c', 'Users', USERNAME, 'Desktop'])
    _Movies = sep.join(['', 'cygdrive', 'c', 'Users', USERNAME, 'Videos'])
    _Music = sep.join(['', 'cygdrive', 'c', 'Users', USERNAME, 'Music'])
    _Pictures = sep.join(['', 'cygdrive', 'c', 'Users', USERNAME, 'Pictures'])
    _Public = sep.join(['', 'cygdrive', 'c', 'Users', 'Public'])
    _UserApps = sep.join(['', 'cygdrive', 'c', 'Program Files'])
    _UserBin = sep.join(['', 'usr', 'local', 'bin'])
    _SystemBin = sep.join(['', 'usr', 'local', 'bin'])
    _ExtBasePath = sep + 'cygdrive'
elif 'win' in sys.platform:
    _SystemApps = sep + 'Applications'
    _CygwinHome = sep.join(['', 'cygdrive', 'home'])
    _Desktop = sep.join(['C:', 'Users', USERNAME, 'Desktop'])
    _Documents = sep.join(['C:', 'Users', USERNAME, 'My Documents'])
    _Downloads = sep.join(['C:', 'Users', USERNAME, 'Downloads'])
    _Dropbox = sep.join(['C:', 'Users', USERNAME, 'Dropbox'])
    _GDrive = sep.join(['C:', 'Users', USERNAME, 'Google Drive'])
    _GitHub = HOMEDIR + sep + 'GitHub'
    _HD = 'C:' + sep
    _Home = sep.join(['C:', 'Users', USERNAME])
    _Movies = sep.join(['C:', 'Users', USERNAME, 'My Videos'])
    _Music = sep.join(['C:', 'Users', USERNAME, 'My Music'])
    _Pictures = sep.join(['C:', 'Users', USERNAME, 'My Pictures'])
    _Public = sep.join(['C:', 'Users', 'Public'])
    _UserApps = sep.join(['C:', 'Users', USERNAME, 'Applications'])
    _UserBin = sep.join(['C:', 'Users', USERNAME, 'Bin'])
    _SystemBin = sep.join(['C:', 'Program Files'])
    _ExtBasePath = ''
else:
    # Assume platform is a linux distribution
    _SystemApps = sep + 'Applications'
    _CygwinHome = None
    _Desktop = HOMEDIR + sep + 'Desktop'
    _Documents = HOMEDIR + sep + 'Documents'
    _Downloads = HOMEDIR + sep + 'Downloads'
    _Dropbox = HOMEDIR + sep + 'Dropbox'
    _GDrive = HOMEDIR + sep + 'Google Drive'
    _GitHub = HOMEDIR + sep + 'GitHub'
    _HD = sep
    _Home = HOMEDIR
    _Movies = HOMEDIR + sep + 'Movies'
    _Music = HOMEDIR + sep + 'Music'
    _Pictures = HOMEDIR + sep + 'Pictures'
    _Public = HOMEDIR + sep + 'Public'
    _UserApps = HOMEDIR + sep + 'Applications'
    _UserBin = HOMEDIR + sep + 'bin'
    _SystemBin = sep.join(['', 'usr', 'local', 'bin'])
    _ExtBasePath = sep + 'Volumes'


# Defined as a function to increase readability within each function
def _try_chdir(dir_path):
    try:
        os.chdir(str(dir_path))
        return True
    except OSError:
        return False


# This function exists to help expand supported platforms
# Calling the function will print a set of errors if there are issues to work through
def platform_warning():
    if N_PLAT_WARN:
        print(""
              "sys.platform = %s"
              "N_PLATFORM   = %s"
              ""
              "Your platform is not directly supported and is assumed to be linux based."
              "Directory structures vary by OS, which can be difficult to detect without user input."
              "Please send this information to:"
              "%s at %s" % (sys.platform, N_PLATFORM, __author__, __email__))
        return False
    else:
        return True


# Utility functions
def count(count_items, return_list=False):
    item_list = []
    for item in count_items:
        if '*' in item:
            item_list += glob(item)
        else:
            item_list.append(item)
    # Force list of items to be unique
    item_list = list(set(item_list))
    if return_list:
        return item_list
    else:
        return len(item_list)


# == These functions map to directories that exist on all platforms by default == #
def apps(mode='return'):
    if mode == 'return':
        return _SystemApps
    else:
        return _try_chdir(_SystemApps)
applications = apps


def desktop(mode='return'):
    if mode == 'return':
        return _Desktop
    else:
        return _try_chdir(_Desktop)


def documents(mode='return'):
    if mode == 'return':
        return _Documents
    else:
        return _try_chdir(_Documents)
mydocuments = documents
my_documents = documents


def downloads(mode='return'):
    if mode == 'return':
        return _Downloads
    else:
        return _try_chdir(_Downloads)


def hd(mode='return'):
    if mode == 'return':
        return _HD
    else:
        return _try_chdir(_HD)


def home(mode='return'):
    if mode == 'return':
        return _Home
    else:
        return _try_chdir(_Home)


def movies(mode='return'):
    if mode == 'return':
        return _Movies
    else:
        return _try_chdir(_Movies)
myvideos = movies
my_videos = movies
videos = movies


def music(mode='return'):
    if mode == 'return':
        return _Music
    else:
        return _try_chdir(_Music)
mymusic = music
my_music = music


def pictures(mode='return'):
    if mode == 'return':
        return _Pictures
    else:
        return _try_chdir(_Pictures)
mypictures = pictures
my_pictures = pictures


def public(mode='return'):
    if mode == 'return':
        return _Public
    else:
        return _try_chdir(_Public)


def systembin(mode='return'):
    if mode == 'return':
        return _SystemBin
    else:
        return _try_chdir(_SystemBin)


def extdrive(drive_name, mode='return'):
    if mode == 'return':
        return drive_name
    else:
        if N_PLATFORM == 'darwin' or N_PLATFORM == 'linux':
            return _try_chdir(_ExtBasePath + sep + drive_name)
        elif N_PLATFORM == 'cygwin':
            return _try_chdir(_ExtBasePath + sep + drive_name.lower())
        elif N_PLATFORM == 'windows':
            return _try_chdir(drive_name.upper() + ':' + sep)
        else:
            return False
extvol = extdrive
extvolume = extdrive


# == These functions map to directories that only exist if specific software is installed == #
def dropbox(mode='return'):
    if mode == 'return':
        return _Dropbox
    else:
        return _try_chdir(_Dropbox)


def gdrive(mode='return'):
    if mode == 'return':
        return _GDrive
    else:
        return _try_chdir(_GDrive)
google_drive = gdrive
google_drive = gdrive


def github(mode='return'):
    if mode == 'return':
        return _GitHub
    else:
        return _try_chdir(_GitHub)


def userbin(mode='return'):
    if mode == 'return':
        return _UserBin
    else:
        return _try_chdir(_UserBin)


def userapps(mode='return'):
    if mode == 'return':
        return _UserApps
    else:
        return _try_chdir(_UserApps)
user_applications = userapps


# == These functions map to directories that are each a special case and require special validation == #
def cyghome(mode='return'):
    if mode == 'return':
        return _CygwinHome
    else:
        return _try_chdir(_CygwinHome)