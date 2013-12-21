import os
import sys
import getpass


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt'


# Define platform specific information
if ('darwin' or 'nix') in sys.platform:
    _SystemApps = os.sep + 'Applications'
    _CygwinHome = None
    _Desktop = os.path.expanduser('~') + os.sep + 'Desktop'
    _Documents = os.path.expanduser('~') + os.sep + 'Documents'
    _Downloads = os.path.expanduser('~') + os.sep + 'Downloads'
    _Dropbox = os.path.expanduser('~') + os.sep + 'Dropbox'
    _GDrive = os.path.expanduser('~') + os.sep + 'Google_Drive'
    _GitHub = os.path.expanduser('~') + os.sep + 'GitHub'
    _HD = os.sep
    _Home = os.path.expanduser('~')
    _Movies = os.path.expanduser('~') + os.sep + 'Movies'
    _Music = os.path.expanduser('~') + os.sep + 'Music'
    _Pictures = os.path.expanduser('~') + os.sep + 'Pictures'
    _Public = os.path.expanduser('~') + os.sep + 'Public'
    _UserApps = os.path.expanduser('~') + os.sep + 'Applications'
    _UserBin = os.path.expanduser('~') + os.sep + 'bin'
    _SystemBin = os.sep.join(['', 'usr', 'local', 'bin'])
    _ExtBasePath = os.sep + 'Volumes'
elif 'cygwin' in sys.platform:
    _SystemApps = os.sep.join(['', 'cygdrive', 'c', 'Program Files'])
    _CygwinHome = os.sep.join(['', 'cygdrive', 'c', 'home', getpass.getuser()])
    _Desktop = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Desktop'])
    _Documents = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Documents'])
    _Downloads = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Downloads'])
    _Dropbox = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Dropbox'])
    _GDrive = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Google_Drive'])
    _GitHub = os.path.expanduser('~') + os.sep + 'GitHub'
    _HD = os.sep.join(['', 'cygdrive', 'c'])
    _Home = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Desktop'])
    _Movies = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Videos'])
    _Music = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Music'])
    _Pictures = os.sep.join(['', 'cygdrive', 'c', 'Users', getpass.getuser(), 'Pictures'])
    _Public = os.sep.join(['', 'cygdrive', 'c', 'Users', 'Public'])
    _UserApps = os.sep.join(['', 'cygdrive', 'c', 'Program Files'])
    _UserBin = os.sep.join(['', 'usr', 'local', 'bin'])
    _SystemBin = os.sep.join(['', 'usr', 'local', 'bin'])
    _ExtBasePath = os.sep + 'cygdrive'
elif 'win' in sys.platform:
    _SystemApps = os.sep + 'Applications'
    _CygwinHome = os.sep.join(['', 'cygdrive', 'home'])
    _Desktop = os.sep.join(['C:', 'Users', getpass.getuser(), 'Desktop'])
    _Documents = os.sep.join(['C:', 'Users', getpass.getuser(), 'My Documents'])
    _Downloads = os.sep.join(['C:', 'Users', getpass.getuser(), 'Downloads'])
    _Dropbox = os.sep.join(['C:', 'Users', getpass.getuser(), 'Dropbox'])
    _GDrive = os.sep.join(['C:', 'Users', getpass.getuser(), 'Google_Drive'])
    _GitHub = os.path.expanduser('~') + os.sep + 'GitHub'
    _HD = 'C:' + os.sep
    _Home = os.sep.join(['C:', 'Users', getpass.getuser()])
    _Movies = os.sep.join(['C:', 'Users', getpass.getuser(), 'My Videos'])
    _Music = os.sep.join(['C:', 'Users', getpass.getuser(), 'My Music'])
    _Pictures = os.sep.join(['C:', 'Users', getpass.getuser(), 'My Pictures'])
    _Public = os.sep.join(['C:', 'Users', 'Public'])
    _UserApps = os.sep.join(['C:', 'Users', getpass.getuser(), 'Applications'])
    _UserBin = os.sep.join(['C:', 'Users', getpass.getuser(), 'Bin'])
    _SystemBin = os.sep.join(['C:', 'Program Files'])
    _ExtBasePath = ''
else:
    print("FS Nav WARNING: Unsupported platform: %s" % sys.platform)
    # Assume platform is a linux distribution
    _SystemApps = os.sep + 'Applications'
    _CygwinHome = None
    _Desktop = os.path.expanduser('~') + os.sep + 'Desktop'
    _Documents = os.path.expanduser('~') + os.sep + 'Documents'
    _Downloads = os.path.expanduser('~') + os.sep + 'Downloads'
    _Dropbox = os.path.expanduser('~') + os.sep + 'Dropbox'
    _GDrive = os.path.expanduser('~') + os.sep + 'Google_Drive'
    _GitHub = os.path.expanduser('~') + os.sep + 'GitHub'
    _HD = os.sep
    _Home = os.path.expanduser('~')
    _Movies = os.path.expanduser('~') + os.sep + 'Movies'
    _Music = os.path.expanduser('~') + os.sep + 'Music'
    _Pictures = os.path.expanduser('~') + os.sep + 'Pictures'
    _Public = os.path.expanduser('~') + os.sep + 'Public'
    _UserApps = os.path.expanduser('~') + os.sep + 'Applications'
    _UserBin = os.path.expanduser('~') + os.sep + 'bin'
    _SystemBin = os.sep.join(['', 'usr', 'local', 'bin'])
    _ExtBasePath = os.sep + 'Volumes'


# Defined as a function to increase readability within each function
def _try_chdir(dir_path):
    try:
        os.chdir(str(dir_path))
        return True
    except OSError:
        return False


# Utility functions
def count():
    pass


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
            function_return = _try_chdir(_ExtBasePath + os.sep + drive_name)
        elif 'cygwin' in sys.platform:
            function_return = _try_chdir(_ExtBasePath + os.sep + drive_name.lower())
        elif 'Windows' in sys.platform:
            function_return = _try_chdir(drive_name.upper() + ':' + os.sep)
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


# Allow for cross platform nomenclature and other increased uability
def mydocuments(mode='return'):
    return documents(mode=mode)


def mymusic(mode='return'):
    return music(mode=mode)


def mypictures(mode='return'):
    return pictures(mode=mode)


def myvideos(mode='return'):
    return movies(mode=mode)


def videos(mode='return'):
    return movies(mode=mode)