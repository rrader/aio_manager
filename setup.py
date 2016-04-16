from setuptools import setup, find_packages


classifiers = [
    'License :: OSI Approved :: BSD License',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Environment :: Web Environment',
    'Development Status :: 4 - Beta',
]


setup(name='aio_manager',
      version='0.1',
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
      extras_require={'sa': ['sqlalchemy>=0.9'], },
      provides=['aio_manager'],
      include_package_data = True,
      test_suite="tests.test_manager")
