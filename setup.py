#!/usr/bin/env python

from distutils.core import setup

setup(name='deep-belief-network',
      version='0.2.0',
      description='Python implementation of Deep Belief Networks',
      packages=['dbn'],
      install_requires=['numpy>=1.9.2',
                        'scipy>=0.16.1',
                        'scikit-learn>=0.16.1',
                        'tensorflow>=0.9.0']
      )
