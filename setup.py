#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name             = 'jamos-toolkit',
    version          = '1.7',
    description      = 'Jamos separator',
    author           = 'Jaeyeon Baek',
    author_email     = 'oops.jybaek@gmail.com',
    url              = 'https://github.com/jybaek/jamos-toolkit',
    download_url     = '',
    install_requires = [],
    packages         = find_packages(include=["jamostoolkit*"]),
    keywords         = ['jamos', 'toolkit', 'separator'],
    python_requires  = '>=3',
    package_data     = {},
    zip_safe         = False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
