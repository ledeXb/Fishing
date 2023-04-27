#!/usr/bin/env python

from setuptools import setup

version = open("files/version.txt").read().strip()
long_description = open("README.md").read().strip()

setup(
    name='Fishing',
    version=version,
    description='Ultimate phishing tool in python with dual tunneling, 77 templates and many more!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='ledeXb',
    author_email='ghbartw@gmail.com',
    license="MIT",
    url='https://github.com/ledeXb/Fishing.git',
    scripts=['Fishing'],
    install_requires=["requests", "bs4", "rich"]
)
