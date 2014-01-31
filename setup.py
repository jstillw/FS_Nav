#!/usr/bin/env python


from os import sep
from glob import glob
from distutils.core import setup


# Build information
__author__ = 'Kevin Wurster'
__version__ = '0.1'
__email__ = 'wursterk@gmail.com'
__license__ = 'See LICENSE.txt from original distribution'


setup(name='FS_Nav',
      version='0.1',
      description='Simple framework and tools for navigating the command line',
      author=__author__,
      author_email=__email__,
      url='https://github.com/geowurster/FS_Nav',
      packages=['fsnav'],
      scripts=glob('bin' + sep + '*'),
      tests='tests'
      )