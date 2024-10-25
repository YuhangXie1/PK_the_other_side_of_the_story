#
# pkmodel setuptools script
#
from setuptools import setup, find_packages

    
def get_version():
    """
    Get version number from the pkmodel module.

    The easiest way would be to just ``import pkmodel ``, but note that this may
    fail if the dependencies have not been installed yet. Instead, we've put
    the version number in a simple version_info module, that we'll import here
    by temporarily adding the oxrse directory to the pythonpath using sys.path.
    """
    import os
    import sys

    sys.path.append(os.path.abspath('pkmodel'))
    from pkmodel.version_info import VERSION as version
    sys.path.pop()

    return version


def get_readme():
    """
    Load README.md text for use as description.
    """
    with open('README.md') as f:
        return f.read()


# Go!
setup(
    # Module name (lowercase)
    name='pkmodel',

    # Version
    version=get_version(),

    description='Solve a multi-compartment pharmacokinetic model',

    long_description=get_readme(),

    license='MIT license',

    author='BBSRC DTP Students from the Other Side',

    # author_email='',

    # maintainer='Martin Robinson',

    # maintainer_email='martin.robinson@cs.ox.ac.uk',

    url='https://github.com/YuhangXie1/PK_the_other_side_of_the_story',

    # Packages to include
    packages=find_packages(include=('pkmodel', 'pkmodel.*')),

    # List of dependencies
    install_requires=[
        "contourpy==1.3.0",
        "cycler==0.12.1",
        "fonttools==4.54.1",
        "iniconfig==2.0.0",
        "kiwisolver==1.4.7",
        "matplotlib==3.9.2",
        "numpy==2.0.2",
        "packaging==24.1",
        "pillow==11.0.0",
        "pluggy==1.5.0",
        "pyparsing==3.2.0",
        "python-dateutil==2.9.0.post0",
        "PyYAML==6.0.2",
        "schema==0.7.7",
        "scipy==1.13.1",
        "setuptools==75.2.0",
        "six==1.16.0",
    ],
    extras_require={
        'docs': [
            # Sphinx for doc generation. Version 1.7.3 has a bug:
            'sphinx>=1.5, !=1.7.3',
            # Nice theme for docs
            'sphinx_rtd_theme',
        ],
        'dev': [
            # Flake8 for code style checking
            'flake8>=3',
            'pytest==8.3.3',
        ],
    },
)
