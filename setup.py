#!/usr/bin/env python
"""The setup script."""
from typing import List

from setuptools import find_packages
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements: List[str] = []

setup_requirements = ['pytest-runner']

test_requirements = ['pytest>=3']

setup(
    author="Ammar Najjar",
    author_email='najjarammar@protonmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Github gist CLI",
    entry_points={
        'console_scripts': [
            'gist=gist.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='gist',
    name='gist',
    packages=find_packages(include=['gist', 'gist.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ammarnajjar/gist',
    version='0.1.0',
    zip_safe=False,
)
