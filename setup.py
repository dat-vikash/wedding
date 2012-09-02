#!/usr/bin/env python
from setuptools import setup, find_packages

required_modules = [
    "django == 1.4.1",
]


setup(
    name="wedding app",
    version="0.1",
    description="Melissa and Vik's wedding app",
    author="Vikash Dat",
    author_email="dat.vikash@gmail.com",
    packages=find_packages(exclude=['test']),
    install_requires=required_modules
)
