.. highlight:: rst

======
FS_Nav
======

File System Navigation for Python 2.6+ and 3+

A set of command line utilities built on a python library designed to make navigating
the command line easier and more user friendly for beginners.

Want to get to your desktop?  Just type "desktop" on the command line and press return.
Want to get to your home directory?  Just type "home" on the command line and press return.
Want to get to your Dropbox directory?  Just type "home" on the command line and press return.
...


----------
Installing
----------
If installing on Windows or Cygwin, read the "Notes about Windows Support" section first.

If you are extremely familiar with the command line, read the "Technical Notes and Advanced Users"
section first.

With `pip http://www.pip-installer.org/en/latest/installing.html`_ (recommended):
    pip install ``fsnav`` –install-option="-install-scripts=/usr/local/bin"

From source:
    Download the latest release from: https://github.com/geowurster/FS_Nav/releases
    Unzip the download
    cd into the unzipped directory
    python run_tests.py --test-src
    python setup.py install --install-scripts=/usr/local/bin

Some of the examples in this document assume the user has downloaded the source code from GitHub,
regardless of the actual installation method.


----------------
Navigation Setup
----------------
FS_Nav contains several components:
* ``fsnav`` - A python module containing a set of functions for file system navigation
* ``nav.py`` - A utility built on ``fsnav`` that exposes parts of the overall intended functionality
* fsnav_generator.sh - A shell script that implements the actual intended functionality
* ``count.py`` - A utility for quickly counting items on the file system

If you just want to enable the navigation functionality listed in the short description of the
beginning of this readme, execute the following after installation:
    ``nav.py`` add_to_profile

Then close your command line window, open another, and execute the following:
    desktop
    pwd

The command line output should be the path to your desktop, and should look like the following:
    $ desktop
    $ pwd
    /Users/YOUR_USERNAME/Desktop
    $

Here's what just happened:
* ``nav.py`` edited your command line profile to include a call to fsnav_generator.sh whenever a new
  session starts.
* Every time you open a new command line window, fsnav_generator.sh creates a set of functions
  that can be used to navigate around the file system without having to cd /path/to/directory
* These functions are limited to a specific set of directories, and can be viewed two ways:
    fsnav_generator.sh --functions
    ``nav.py`` --codes
  Because the GitHub desktop application installs a command line utility called 'github',
  only ``nav.py`` can
  In general the function names are intuitive (eg. 'documents' for your documents directory),
  although a few must be renamed (github => ghub) to prevent clashing with other existing command
  line utilities.


--------------
nav.py Utility
--------------
Just calling ``nav.py`` will print out a directory path:
    ``nav.py`` desktop
This script can't do any directory changing by default, but it can be enabled with back ticks
and a call to 'cd':
    cd `nav.py desktop`
It can also easily be incorporated into shell scripts:
    DESKTOP_DIR=`nav.py desktop`


--------
count.py
--------
A simple utility for counting files and directories on the command line.  For more information, do:
    ``count.py`` --help
Some sample usages are listed below and assume the user's current working directory is FS_Nav's root
package directory.
    $ count.py
    9
    $ ``count.py`` bin/
    1
    $ ``count.py`` bin/*
    3
    $ ``count.py`` * bin/*
    12


------------
fsnav Module
------------

Note that if you installed FS_Nav from source code instead of pip, the counts below will be slightly
off due to the 'build' directory created by running:
    python setup.py install --install-scripts=/usr/local/bin
FS_Nav/build can safely be deleted to make the tutorials match.

When calling count.py, the command line input is passed directly to a function within the ``fsnav`` module.
Navigate to the root directory of the FS_Nav package and do the following:
    $ ``count.py`` * bin/*
    12
This is the same as doing the following in Python:
    > import fsnav
    > fsnav.count(['*', 'bin/*'])
    12
Optionally, the count function will return a ``list`` of the items it is counting:
    > import fsnav
    > fsnav.count(['*', 'bin/*'], return_list=True)
    ['bin', 'fsnav', 'tests', 'bin/nav.py', 'bin/fsnav_generator.sh', 'bin/count.py', 'run_tests.py',
     'README.rst','CHANGES.txt', 'setup.py', 'LICENSE.txt', 'README.txt']

When calling nav.py, the user supplies a code, which ``nav.py`` uses to figure out which ``fsnav`` function
it should call.  Execute the following on the command line:
    ``nav.py`` desktop
This is the same as doing the following in Python:
    > import fsnav
    > fsnav.desktop()
    '/Users/username/Desktop'
Alternatively, these functions can be used for file system navigation within python scripts.  Each
navigation function accepts a parameter called ``mode``, that when set to ``mode='cd'``, tells the function
to actually change directories.  If the function successfully changes directories, it returns ``True``, and
otherwise returns ``False``.
    > import fsnav
    > print(fsnav.desktop())
    '/Users/username/Desktop'

Functions and example output:
    > import fsnav
    > fsnav.apps()
    '/Applications'
    > fsnav.desktop()
    '/Users/username/Desktop'
    > fsnav.documents()
    '/Users/username/Documents'
    > fsnav.downloads()
    '/Users/username/Downloads'
    > fsnav.hd()
    '/'
    > fsnav.home()
    '/Users/username'
    > fsnav.movies()
    '/Users/username/Movies'
    > fsnav.music()
    '/Users/username/Music'
    > fsnav.pictures()
    '/Users/username/Pictures'
    > fsnav.public()
    '/Users/username/Public'
    > fsnav.systembin()
    '/usr/local/bin'
    > fsnav.dropbox()
    '/Users/username/Dropbox'
    > fsnav.gdrive()
    '/Users/username/Google Drive'
    > fsnav.github()
    '/Users/username/GitHub'
    > fsnav.userbin()
    '/Users/username/bin'
    > fsnav.userapps()
    '/Users/username/Applications'
    > fsnav.cyghome()
    >


---------------------------
Notes about Windows Support
---------------------------

Here's the short story:
Windows is not fully supported, although everything should work fine on `Cygwin http://www.cygwin.com`_.
If there is enough demand, I'm happy to figure out how to support the Windows command line.

The Windows command line is currently not completely supported as I do not have consistent access to a
machine to verify everything.  As far as I know, ``nav.py`` and ``count.py`` should work without issue,
but ``fsnav_generator.sh`` is a bash shell script and does not work, which means that the navigation
functions cannot be generated.


----------------------------------
Technical Notes and Advanced Users
----------------------------------

Sub-shell's can't do anything to the parent process, which is why ``nav.py`` can't be used for
navigation.  The ``fsnav_generator.sh`` script creates a set of functions that call ``nav.py``
to get a directory path, and cd to it.  These functions only stick around in the parent process
if ``fsnav_generator.sh`` is called with ``source``.  Here's what the functions look like:
    function desktop() { cd `nav.py desktop` ; }