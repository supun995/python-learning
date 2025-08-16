Introduction
Packaging Python-based applications has evolved over time. Up until Python 3.12 the standard library included a packaging library called distutils.

Here's how Python's documentation describes disutils:

The distutils package provides support for building and installing additional modules into a Python installation. The new modules may be either 100%-pure Python, or may be extension modules written in C, or may be collections of Python packages which include modules coded in both Python and C.

— 
Building and installing Python modules
, opens in a new tab

The distutils package introduced the setup.py file as an entry-point for performing build steps. The setup.py file contained build logic and was executed as a command line application. Over time the distutils package became out of sync with the needs of the Python community. The third-party setuptools library was created on top of distutils to provide missing functionality. The setuptools module provides mechanisms for locating source files to package and producing package files.

Example setup.py using setuptools:

Copy code
from setuptools import setup, find_packages

setup(
    name='fake',
    version='2.1.1',
    packages=find_packages(include=['fake', 'fake.*'])
)

The use of setuptools and the setup.py file remained Python's packaging solution for years. Over time the downsides of this solution began to impact the Python community. Package installations relied on the host's Python environment and third-party modules. This caused version conflicts with third-party modules such as setuptools used by the installer. Developers were unable to rely on specific features from build modules. For example, an older version of setuptools in a host's environment could cause installation errors if an installer used newer features.

The Python community was in need of a better packaging solution. An alternative approach was defined in PEPs 
0517
, opens in a new tab and 
0518
, opens in a new tab. These PEPs represent the current solution for Python packaging. The new packaging solution deprecates the distutils library in favor of third-party options. The approach defined in these PEPs advocates for two processes. One process produces an isolated build environment. The other process performs build steps inside the isolated build environment. These two processes represent the concepts of build front-ends and back-ends.

Build front-ends are responsible for establishing isolated Python environments with any required build dependencies installed. Build back-ends are hooks called by the front-end in order to produce source and distribution packages.

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

Instructions
The pyproject.toml file allows project specific metadata to be specified under the project table. The allowed properties are defined in [PEP-0621(
https://peps.python.org/pep-0621/
, opens in a new tab). These properties are build-system independent.

Add the following code to the webapp/pyproject.toml file.

Copy code
[project]
name            = "cloudacademy"
version         = "0.0.1"



When pip installs a package it also installs all required dependencies. The dependencies property accepts a list of requirement specifiers that define the runtime dependencies of the package.

Append the dependencies to the project table.

Copy code
dependencies    = [
    "rich",
    "Flask",
    "Pillow",
    "bcrypt"
]




Open the built-in terminal pane (Terminal > New Terminal).




A build front-end is required in order to read the pyproject.toml file and interact with a build back-end. Multiple build front-ends exist in the Python community. The 
build
, opens in a new tab library is a minimalist build front-end.

Install the build front-end.

Copy code
python3 -m pip install build



Currently the pyproject.toml file only contains project related information and no build system details. Build front-ends use default settings for optional tables and properties. The setuptools library is used as the default build back-end.

Running the build process now will result in the front-end using the default setuptools back-end. The setuptools module includes its own default settings that determine which files to include in the packages.

Build the application.

Copy code
python3 -m build ./webapp



...




By default the build front-end creates both source and distribution packages into the dist/ directory. However, they can be created independently and into other directories with the 
--outdir
, opens in a new tab flag.

Observe the build artifacts.

Copy code
ls -lash webapp/dist



The .whl file is the distribution package and the compressed .tar.gz file is the source distribution.

Build system details are defined in the build-system table. The requires property is used to install build system packages such as build back-ends. The property accepts a list of requirement specifiers as strings. The build-backend property accepts a string pointing to the build back-end module. The values defined below were found in the setuptools
documentation
, opens in a new tab.

Breaking the build process into a front-end and back-end allows build dependencies to be isolated from the host Python environment.

The following table and associated properties explicitly define the build system to use setuptools. These settings could be omitted since they match the default values. However, explicit settings for important tables such as build-system can provide context to future maintainers.

Append the following code to the webapp/pyproject.toml file.

Copy code
[build-system]
requires        = ["setuptools"]
build-backend   = "setuptools.build_meta"




The default settings of setuptools is causing some directories/files to be omitted from the packages. Specifically the static/ and templates/ directories.

Re-build the application to review the build output.




Notice the listing of added files doesn't include files located in the missing directories. Each back-end defines its own configuration settings for details such as which files to include in the packages. The setuptools module includes 
rules
, opens in a new tab for determining which files to package. The use of a 
MANIFEST.in
, opens in a new tab file allows setuptools finer control over the included and excluded files. The MANIFEST.in file specifies a listing of file inclusion / exclusion commands. The graft command used below includes entire directories.

Add the following code to the webapp/MANIFEST.in file.

Copy code
graft webapp/templates
graft webapp/static



Re-build the application to review the build output.




Notice the directories are now included in the listing. The application is now ready to be installed into a separate virtual environment to verify that the packages behave as expected once installed.

Split the terminal (Terminal > Split Terminal).




Going forward the left terminal window is designated the build terminal and the right terminal the install terminal.

Using the install terminal, create and activate a virtual environment.

Copy code
python3 -m venv install_env
deactivate
source install_env/bin/activate
The webapp/webapp/__init__.py file includes a print statement at the top of the file which displays the text: greetings from webapp. Importing the module will result in the message being printed to the console. This is going to be used to determine the success of the package installation.

(install terminal) Observe that the cloudacademy package is currently uninstalled in this virtual environment.

Copy code
python3 -m pip show cloudacademy



(install terminal) Install the distribution package.

Copy code
python3 -m pip install webapp/dist/cloudacademy-0.0.1-py3-none-any.whl



(install terminal) Verify that the package was successfully installed.

Copy code
python3 -m pip show cloudacademy
python3 -c "import webapp"



The pyproject.toml file includes a table named tools that allows supported Python packages from PyPI to be configured using a period to separate namespaces. This table commonly configures build back-ends, linters, code coverage modules, etc.

Libraries such as setuptools, pytest, autopep8, among others already support using the tools table as a configuration mechanism.

Using the (build terminal) Install the autopep8 package.

Copy code
python3 -m pip install autopep8



Append the following table to the webapp/pyproject.toml file.

Copy code
[tool.autopep8]
max_line_length = 120
in-place        = true
recursive       = true
aggressive      = 3
exclude         = "*/build/**,*.egg-info"




(build terminal) Run autopep8 against the webapp Python package.

Copy code
autopep8 -v webapp/



Notice the first few lines of output from autopep8 indicate that the settings were found in the pyproject.toml file. Support for additional third-party libraries will expand as the Python community continues to invest in using the pyproject.toml file.

Summary
The current evolution of Python packaging uses a pyproject.toml file to define project metadata, build system requirements, and third-party tool configuration. Build front-ends create isolated Python build environments used by back-ends to create packages.

The build module serves as a minimalist build front-end. The setuptools module serves as a build back-end in addition to supporting the previous distutils solution. Other options exist for both front and back end processes.

Multiple third-party packaging libraries exist in the Python ecosystem. 
Poetry
, opens in a new tab has become popular due to its more advanced features such as dependency resolution, lock file creation, etc. 
Flit
, opens in a new tab is has become popular as the simplest way to push packages to 
PyPI
, opens in a new tab.

The choice to move away from distutils in favor of a standards-based approach allows software engineers to select the best options for each project.