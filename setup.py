#!/usr/bin/env python
from setuptools import find_packages
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['requests', ]

test_requirements = ['pytest>=3', ]

setup(
    author='dingtalk',
    author_email='ibopo@126.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description='.',
    install_requires=requirements,
    license='MIT license',
    long_description=readme + '\n\n',
    include_package_data=True,
    keywords='dingtalk',
    name='dingtalk',
    packages=find_packages(include=['dingtalk', 'dingtalk.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bopo/dingtalk',
    version='0.1.0',
    zip_safe=False,
)
