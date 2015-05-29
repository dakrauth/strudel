#!/usr/bin/env python
import os, sys
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit(0)

with open('README.rst', 'r') as f:
    long_description = f.read()

# Dynamically calculate the version based on swingtime.VERSION.
version = __import__('strudel').__version__

setup(
    name='strudel',
    url='https://github.com/dakrauth/strudel',
    author='David A Krauth',
    author_email='dakrauth@gmail.com',
    description='Simple tools for downloading, cleaning, extracting and parsing content',
    version=version,
    long_description=long_description,
    platforms=['any'],
    license='MIT License',
    py_modules=['choice_enum'],
    classifiers=(
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ),
)