"""This file makes our hooks easy to install by pre-commit.
Python packages seem to be the dominating way hooks can be installed as.
There's also support for node.js and ruby packages as well as docker images.
From what I understood there was no support for something like make.

See docs here:
http://pre-commit.com/#usage
And here:
http://pre-commit.com/#new-hooks
"""
from setuptools import setup


setup(
    # any random silly name for our dummy python package.
    name='pre_commit_hook_prototype',
    version='0.0.0',
    # This installs the dependencies
    install_requires=['yapf==0.16.1', 'docformatter==0.8'],
    # This places our yapf.conf in the right place
    data_files=[('etc', ['egym_yapf.conf'])]
)
