#!/usr/bin/env python
# -*- coding: utf-8 -*-

from supervisorclusterctl import __version__, __author__, __programm_name__, __programm_description__
import os
import sys
try:
    from setuptools import setup, find_packages
except ImportError:
    print "supervisorclusterctl needs setuptools in order to build. " \
          "Please install it using your package manager (usually python-setuptools) or via pip (pip install setuptools)."
    sys.exit(1)

requirements = []

test_requirements = []

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except:
    README = ''
    CHANGES = ''

data_files = [('/etc/ansible', ['config/hosts'])]

setup(
    name=__programm_name__,
    version=__version__,
    description=__programm_description__,
    long_description=README + '\n\n' +  CHANGES,
    author=__author__,
    keywords = 'SPICA',
    author_email='robert.winkler@telekom.de',
    url='https://ngc.jenk.toon.sul.t-online.de/gitblit/r/spica-cluster-control.git',
    packages=find_packages(exclude=["docs", "test"]),
    install_requires=requirements,
    tests_require=test_requirements,
    data_files=data_files,
    entry_points={
     'console_scripts': [
         'supervisorclusterctl = supervisorclusterctl.supervisorclusterctl:main'
        ],
    }
)