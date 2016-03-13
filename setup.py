#!/usr/bin/env python

from distutils.core import setup
import sys

sys.path.append('./mesh')

setup(name='mesh',
      version='0.1',
      description='Utilities for area mesh code definted in Japanese Industorial Standards (JIS X 0410 地域メッシュコード).',
      author='Haruki Nishikawa',
      author_email='',
      url='',
      packages=['mesh'],
     )
