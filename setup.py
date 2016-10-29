# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('password_creator/password_creator.py').read(), re.M).group(1)

setup(
    name="password_creator",
    packages=["password_creator"],
    entry_points={"console_scripts": ['password_creator = password_creator.password_creator:main']},
    version=version,
    description="Create random passwords from the command line",
    long_description="Create random passwords using a dictionary of close to one hundred thousand English words",
    author="Patrick Lewery Harris",
    author_email="patrick@plh.io",
    url="https://github.com/patrickleweryharris/password_creator",)
