#!/usr/bin/python

import tempfile
import sys
import os

__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, Canari Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'


# Import modules relative to where this script is if necessary
my_location = os.path.dirname(__file__)
os.chdir(my_location)
sys.path.append(my_location)

# Use temporary directory as Python Egg Cache
os.environ['PYTHON_EGG_CACHE'] = tempfile.gettempdir()

# Import our Flask app
from plume import app as application
