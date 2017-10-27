#! /usr/bin/env python
"""aio_manager package setuptools installer."""

from setuptools import setup, find_packages


classifiers = [
    'License :: OSI Approved :: BSD License',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Environment :: Web Environment',
    'Development Status :: 4 - Beta',
]

extras_require = {'sa': ['sqlalchemy>=0.9']}
extras_require['postgres'] = ['psycopg2>=2.5.2', *extras_require['sa']]
extras_require['mysql'] = ['PyMySQL>=0.7.5', *extras_require['sa']]


__name__ == '__main__' and setup(
    name='aio_manager',
    use_scm_version=True,
    description='Script manager for aiohttp.',
    classifiers=classifiers,
    platforms=['POSIX'],
    author='Roman Rader',
    author_email='antigluk@gmail.com',
    maintainer='Sviatoslav Sydorenko (@webknjaz)',
    url='https://github.com/rrader/aio_manager',
    license='BSD',
    packages=find_packages(),
    install_requires=['aiohttp', 'colorama'],
    extras_require=extras_require,
    setup_requires=['setuptools_scm'],
    python_requires='>=3.5',
    provides=['aio_manager'],
    include_package_data=True,
    test_suite='tests.test_manager'
)
