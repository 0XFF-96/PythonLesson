#!/usr/bin/env python3

"""Factorial projiect"""

from setuptools import find_packages, setup

setup(name = 'factorial',
	version = '0.1',
	description = "Factorial module.",
	long_description = "A test module for our book",
	platforms = ["Linux"],
	author="shiyanlou",
	author_email="support@shiyanlou.com",
	url="https://www.shiyanlou.com/courses/596",
	license = "MIT",
	packages=find_packages()
	)

