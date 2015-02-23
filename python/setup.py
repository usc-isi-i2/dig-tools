# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dig-tools',
    version='0.0.1',
    description='Dig-Tools module for Karma Dig',
    long_description=readme,
    author='Andrew Philpot',
    author_email='andrew.philpot@gmail.com',
    url='https://github.com/InformationIntegrationGroup/dig-tools',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    )
