#!/usr/bin/env python

from setuptools import setup, find_packages

version = '1.0dev'

msg = '''------------------------------
Installing omUtils version {}
------------------------------
'''.format(version)
print(msg)

setup(
    name='omUtils',
    version=version,
    author='lx Gui',
    author_email='guilixuan@gmail.com',
    keywords=['Python'],
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'asyncio',
    ],
)

msg = '''------------------------------
omUtils installation complete!
------------------------------
'''
print(msg)
