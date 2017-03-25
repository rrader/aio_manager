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
extras_require['postgres'] = ['aiopg', *extras_require['sa']]
extras_require['mysql'] = ['aiomysql', *extras_require['sa']]


setup(name='aio_manager',
      version='1.0.1',
      description='Script manager for aiohttp.',
      long_description=('Script manager for aiohttp.\n'
                        'Inspired by Flask-script. Allows to write external scripts. '),
      classifiers=classifiers,
      platforms=['POSIX'],
      author='Roman Rader',
      author_email='antigluk@gmail.com',
      url='https://github.com/rrader/aio_manager',
      license='BSD',
      packages=find_packages(),
      install_requires=['aiohttp', 'colorama'],
      extras_require=extras_require,
      provides=['aio_manager'],
      include_package_data=True,
      test_suite='tests.test_manager')
