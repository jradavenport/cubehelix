#!/usr/bin/env python
# encoding: utf-8

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="cubehelix",
    version="0.1.0",
    author="James Davenport",
    # author_email="",
    description="Cubehelix colormaps for matplotlib",
    long_description=read('README.md'),
    # license="BSD",
    py_modules=['cubehelix'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering :: Visualization",
        # "License :: OSI Approved :: BSD License",
        ]
)
