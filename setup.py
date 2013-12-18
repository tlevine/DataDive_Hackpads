# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name = 'datadive-hackpads',
    version = '0.0.1',
    author = u'Jude Mitchell and Thomas Levine',
    author_email = '_@thomaslevine.com',
    url = 'https://github.com/JudeMitchell/DataDive_Hackpads',
    license = 'AGPL',
    packages = ['hackpad'],
    description = 'Parse hackpads from data dives into pretty JSON.',
#   long_description = open('readme.md').read(),
    install_requires = [
        'requests',
        'nose',
    ],
)
