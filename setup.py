"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='fireo',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
<<<<<<< HEAD
    version='1.5.0',
=======
    version='1.4.2',
>>>>>>> d4f09f1ea97ad32a2c090ed4692b6c2888366d12

    description="FireO ORM is specifically designed for the Google's Firestore.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    # The project's main homepage.
    url="https://github.com/octabytes/FireO",

    # Author details
    author="OctaByte",
    author_email="Dev@octabyte.io",

    # Choose your license
    license="Apache 2.0",

    # See https://pypi.org/classifiers/
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",

        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: Apache Software License",

        # Specify the Python versions you support here. In particular, ensure
<<<<<<< HEAD
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python",
=======
        # that you indicate whether you support Python 3.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
>>>>>>> d4f09f1ea97ad32a2c090ed4692b6c2888366d12
        "Programming Language :: Python :: 3.7"
    ],

    # What does your project relate to?
    keywords='Python Firestore Models ORM Google Cloud Firebase',

    # Add all packages except tests
    packages=find_packages('src', exclude=['tests']),

    package_dir={'': 'src'},

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
<<<<<<< HEAD
    install_requires=['google-cloud-firestore>=2.2.0,<=2.3.4'],
=======
    install_requires=['google-cloud-firestore>=2.1.0'],
>>>>>>> d4f09f1ea97ad32a2c090ed4692b6c2888366d12
)
