"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distripip install buting.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ixnetwork-rest',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.55a51',

    description='IxNetwork REST API Client',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/ajbalogh/ixnetwork_client_python',

    # Author details
    author='andrey.balogh@gmail.com',
    author_email='andrey.balogh@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords='ixnetwork rest automation development',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'utils', 'samples']),
    package_data={'ixnetwork': [
        'samples/*.py',
        'samples/create/*.py',
        'samples/sessions/*.py',
        'samples/global/*.py',
        'samples/emulation_host/*.py',
        'samples/emulation_host/*.ixncfg',
        'samples/query/*.py'
        ]
    },

    # If your project only runs on certain Python versions, 
    # setting the python_requires argument to the appropriate 
    # PEP 440 version specifier string will prevent pip from installing 
    # the project on other Python versions.
    python_requires='>=2.7, <4',

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[],
)
