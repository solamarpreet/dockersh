#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = ['prompt-toolkit>3.0.0',
                'docker>5.0.0',]

test_requirements = [ ]

setup(
    author="Amarpreet Singh",
    author_email='solamarpreet@protonmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    description="A shell for Docker commands with autocomplete & command history",
    entry_points={
        'console_scripts': [
            'dockersh=dockersh.main:cli',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description="For detailed information visit https://github.com/solamarpreet/dockersh",
    include_package_data=True,
    keywords='dockersh',
    name='dockersh',
    packages=find_packages(include=['dockersh', 'dockersh.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/solamarpreet/dockersh',
    version='0.0.1',
    zip_safe=False,
)
