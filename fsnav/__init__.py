import os
import sys
import getpass
from os import sep
from glob import glob

# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__source__ = 'https://github.com/geowurster/FS_Nav'
__license__ = '''
New BSD License

Copyright (c) 2014, Kevin D. Wurster
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* The names of its contributors may not be used to endorse or promote products
  derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''



# Global variables
HOMEDIR = os.path.expanduser('~')
USERNAME = getpass.getuser()
ALIASES = {'apps':      ['System applications', 'apps', 'applications'],
           'desktop':   ['User Desktop', 'desktop'],
           'documents': ['User documents', 'documents', 'mydocuments', 'my_documents'],
           'downloads': ['User downloads', 'downloads', 'download'],
           'hd':        ['Top level of hard drive', 'hd', 'harddrive', 'hard_drive'],
           'home':      ['User home directory', 'home', 'homedir', 'home_dir'],
           'movies':    ['User video', 'movies', 'myvideos', 'my_videos', 'videos'],
           'music':     ['User music', 'music', 'mymusic', 'my_music'],
           'pictures':  ['User pictures', 'pictures', 'mypictures', 'my_pictures'],
           'public':    ['User public (system public on Windows)', 'public'],
           'systembin': ['System bin', 'systembin', 'system_bin'],
           'dropbox':   ['User dropbox', 'dropbox'],
           'gdrive':    ['User Google Drive', 'gdrive', 'google_drive', 'googledrive'],
           'github':    ['User GitHub', 'github (nav.py ONLY)', 'ghub'],
           'userbin':   ['User bin', 'userbin', 'user_bin'],
           'userapps':  ['User applications', 'userapps', 'user_apps'],
           'cyghome':   ['Cygwin home directory (Windows only)', 'cyghome', 'cygwin_home']}
_N_PLAT_WARN = False  # Used in platform_warning() function to determine whether or not current platform is supported
if 'darwin' in sys.platform:
    _N_PLATFORM = 'mac'
elif 'nix' in sys.platform:
    _N_PLATFORM = 'linux'
elif 'win' in sys.platform:
    _N_PLATFORM = 'win'
elif 'cygwin' in sys.platform:
    _N_PLATFORM = 'cygwin'
else:
    _N_PLAT_WARN = True
    _N_PLATFORM = 'linux'


# Define platform specific information
if _N_PLATFORM == 'linux' or _N_PLATFORM == 'mac':
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
elif _N_PLATFORM == 'cygwin':
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
    if _N_PLAT_WARN:
        print(""
              "sys.platform = %s"
              "_N_PLATFORM   = %s"
              ""
              "Your platform is not directly supported and is assumed to be linux based."
              "Directory structures vary by OS, which can be difficult to detect without user input."
              "Please send this information to:"
              "%s at %s" % (sys.platform, _N_PLATFORM, __author__, __email__))
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
ALIASES['apps'].insert(0, apps)


def desktop(mode='return'):
    if mode == 'return':
        return _Desktop
    else:
        return _try_chdir(_Desktop)
ALIASES['desktop'].insert(0, desktop)


def documents(mode='return'):
    if mode == 'return':
        return _Documents
    else:
        return _try_chdir(_Documents)
ALIASES['documents'].insert(0, documents)


def downloads(mode='return'):
    if mode == 'return':
        return _Downloads
    else:
        return _try_chdir(_Downloads)
ALIASES['downloads'].insert(0, downloads)


def hd(mode='return'):
    if mode == 'return':
        return _HD
    else:
        return _try_chdir(_HD)
ALIASES['hd'].insert(0, hd)


def home(mode='return'):
    if mode == 'return':
        return _Home
    else:
        return _try_chdir(_Home)
ALIASES['home'].insert(0, home)


def movies(mode='return'):
    if mode == 'return':
        return _Movies
    else:
        return _try_chdir(_Movies)
ALIASES['movies'].insert(0, movies)


def music(mode='return'):
    if mode == 'return':
        return _Music
    else:
        return _try_chdir(_Music)
ALIASES['music'].insert(0, music)


def pictures(mode='return'):
    if mode == 'return':
        return _Pictures
    else:
        return _try_chdir(_Pictures)
ALIASES['pictures'].insert(0, pictures)


def public(mode='return'):
    if mode == 'return':
        return _Public
    else:
        return _try_chdir(_Public)
ALIASES['public'].insert(0, public)


def systembin(mode='return'):
    if mode == 'return':
        return _SystemBin
    else:
        return _try_chdir(_SystemBin)
ALIASES['systembin'].insert(0, systembin)


# == These functions map to directories that only exist if specific software is installed == #
def dropbox(mode='return'):
    if mode == 'return':
        return _Dropbox
    else:
        return _try_chdir(_Dropbox)
ALIASES['dropbox'].insert(0, dropbox)


def gdrive(mode='return'):
    if mode == 'return':
        return _GDrive
    else:
        return _try_chdir(_GDrive)
ALIASES['gdrive'].insert(0, gdrive)


def github(mode='return'):
    if mode == 'return':
        return _GitHub
    else:
        return _try_chdir(_GitHub)
ALIASES['github'].insert(0, github)


def userbin(mode='return'):
    if mode == 'return':
        return _UserBin
    else:
        return _try_chdir(_UserBin)
ALIASES['userbin'].insert(0, userbin)


def userapps(mode='return'):
    if mode == 'return':
        return _UserApps
    else:
        return _try_chdir(_UserApps)
ALIASES['userapps'].insert(0, userapps)


# == These functions map to directories that are each a special case == #
def cyghome(mode='return'):
    if mode == 'return':
        return _CygwinHome
    else:
        return _try_chdir(_CygwinHome)
ALIASES['cyghome'].insert(0, cyghome)


def extdrive(drive_name, mode='return'):
    if mode == 'return':
        return drive_name
    else:
        if _N_PLATFORM == 'darwin' or _N_PLATFORM == 'linux':
            return _try_chdir(_ExtBasePath + sep + drive_name)
        elif _N_PLATFORM == 'cygwin':
            return _try_chdir(_ExtBasePath + sep + drive_name.lower())
        elif _N_PLATFORM == 'windows':
            return _try_chdir(drive_name.upper() + ':' + sep)
        else:
            return False