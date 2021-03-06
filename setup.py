import os
from setuptools import setup

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(BASE_PATH, 'README.rst')).read()

__version__ = '0.0.1'
__author__ = 'Masashi Shibata <contact@c-bata.link>'
__author_email__ = 'contact@c-bata.link'
__license__ = 'MIT License'
__classifiers__ = (
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Topic :: Internet :: WWW/HTTP :: WSGI',
    'Environment :: Web Environment',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
)


setup(
    name='wsgi-vmprof',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    url='https://github.com/c-bata/wsgi-vmprof',
    description='',
    long_description=README,
    classifiers=__classifiers__,
    py_modules=['wsgi_vmprof'],
    install_requires=['vmprof'],
    keywords='web wsgi vmprof',
    license=__license__,
    include_package_data=True,
    test_suite='tests',
)
