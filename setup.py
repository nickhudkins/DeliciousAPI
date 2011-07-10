#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(name="deliciousapi",
      version="1.0",
      description="Delicious library for python",
      license="MIT",
      author="Michael G. Noll",
      author_email="michael@michael-noll.com",
      url="git@github.com:nickhudkins/DeliciousAPI.git",
      packages = find_packages(),
      keywords= "delicious api",
      zip_safe = True)
