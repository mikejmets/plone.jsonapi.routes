# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

version = '0.7'

long_description = (
    open('README.rst').read()
    + '\n' +
    open(os.path.join('docs', 'HISTORY.rst')).read()
    + '\n')

setup(name='plone.jsonapi.routes',
      version=version,
      description="Plone JSON API -- Routes",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Zope2",
        ],
      keywords='',
      author='Ramon Bartl',
      author_email='ramon.bartl@googlemail.com',
      url='https://github.com/ramonski/plone.jsonapi',
      license='MIT',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['plone', 'plone.jsonapi'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.api',
          'plone.jsonapi.core>=0.3',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
               'plone.app.testing',
               'unittest2',
           ]
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

# vim: set ft=python ts=4 sw=4 expandtab :
