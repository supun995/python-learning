#package is collection of modules.
# module: group code into reusable unit based on shared purpose
# package: group modules into reusable unit based on shared purpose

#import function from package.module

#standard lib - python
#math,os,sys,collections,random, etc

from setuptools import setup, find_packages

setup(
    name='fake',
    version='2.1.1',
    packages=find_packages(include=['fake', 'fake.*'])
)
"""
The Python community was in need of a better packaging solution. An alternative approach was defined in PEPs 
0517
and 
0518
 These PEPs represent the current solution for Python packaging. The new packaging solution deprecates the distutils library in favor of third-party options. The approach defined in these PEPs advocates for two processes. One process produces an isolated build environment. The other process performs build steps inside the isolated build environment. These two processes represent the concepts of build front-ends and back-ends.
 
 There are two primary forms of Python packages: source (sdist) and distribution packages (bdist). Source packages consist of all source files required to run the application bundled into a compressed file. Distribution packages are pre-built 
wheel files
, opens in a new tab with Python packages, modules, and resource files that are ready to install. Both types of packages are installed using 
pip
, opens in a new tab. Distribution packages are typically preferred because unlike source packages they don't require build steps to occur in the host environment.
The current packaging solution foregoes the setup.py file for a pyproject.toml file. The pyproject.toml file contains sections that are referred to as tables with key-value pairs of data referred to in this lab as properties. The pyproject.toml file defines project metadata, build system details, and third-party tool configuration.
Packaging a Python application requires the following:

Python modules and or packages.
A pyproject.toml file.
A build front-end.
A build back-end.

A build front-end is required in order to read the pyproject.toml file and interact with a build back-end. Multiple build front-ends exist in the Python community. The 
build
, opens in a new tab library is a minimalist build front-end. python3 -m pip install build

Currently the pyproject.toml file only contains project related information and no build system details. Build front-ends use default settings for optional tables and properties. The setuptools library is used as the default build back-end.

Running the build process now will result in the front-end using the default setuptools back-end. The setuptools module includes its own default settings that determine which files to include in the packages.

Build the application.

Copy code
python3 -m build ./webapp
"""
