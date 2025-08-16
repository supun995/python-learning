Getting Started With Pip
Pip
, opens in a new tab is a package installer for Python. Pip is used to install packages from the 
Python Package Index
, opens in a new tab, other indexes, local distributions, URLs, and source control systems.

Pip is a Python module commonly used as a CLI (command line interface). It's used to install Python modules and their dependencies.

This lab explores using pip by installing an open 
source
, opens in a new tab package from the Python Package Index named 
rich
, opens in a new tab.

NOTE: The rich module is used to create user-friendly terminal based applications.

Creating Python applications which rely on third-party modules introduces application dependencies which need to be managed.

Dependency management can introduce challenges when different applications require conflicting versions of the same dependent module.

In the example below application_a and application_b require conflicting versions of the same module.

application_a.py

Requires:
rich <= 10.11.0
application_b.py

Requires:
rich >= 12.3
Virtual environments allow application dependencies to be managed independently. Python includes a module called venv which is used to create isolated application environments. Modules installed into virtual environments by pip are specific to each environment.

While not required, virtual environments are recommended because they help to mitigate dependency conflicts.

Instructions
The venv module can be used as a CLI. The command below creates a new virtual environment in a directory named .labenv.

NOTE: Directories beginning with a period are hidden directories on Linux systems.

The prompt flag sets the text used at the beginning of the shell's prompt once the virtual environment is active.

Create a virtual environment in the IDEs terminal pane: (Terminal > New Terminal).

NOTE: This command does not display results if successful.

Copy code
python3 -m venv .labenv --prompt="CloudAcademy Env"
Virtual environments need to be activated. Once activated pip will install dependencies into the virtual environment.

Activate the virtual environment.

Copy code
source .labenv/bin/activate



Pip is installed with most modern versions of Python. The official 
pip installation instructions
, opens in a new tab provide up-to-date details regarding installing pip, should it be missing.

Pip can be invoked using Python's -m argument which runs a module as a script. Using the -m argument is effectively the same as running a script directly. Rather than specifying a filename, the -m argument checks for modules in directories listed in os.path. The -m argument runs the module as __main__.

The --version flag displays version details for the pip module.

Ensure pip is installed.

Copy code
python3 -m pip --version



The pip module requires an occasional upgrade. The module can upgrade itself using the install command with the --upgrade flag.

Ensure pip is up-to-date.

Copy code
python -m pip install --upgrade pip



The --help flag displays CLI help details including commands and arguments.

Display the command line help options.

Copy code
python -m pip --help



The list command displays a listing of installed modules. Notice no module named rich is currently installed.

List the installed modules for the virtual environment.

Copy code
python3 -m pip list

Attempting to run the cloudacademy/playground.py code file before rich is installed raises a ModuleNotFoundError exception.

Run the cloudacademy/playground.py code file.

Copy code
python3 cloudacademy/playground.py


The install command installs a distribution package. Omitting version details when installing a package installs the latest version. The following command installs the latest version of the rich module from the Python Package Index.

The 
Python Package Index
, opens in a new tab is a public repository of Python distribution packages. By default pip looks to this index when installing packages. Around 400,000 projects reside within the index. Projects span a wide range of use cases and license types. Third-party packages can save hours of development effort. However, they may also introduce risk in the form of bugs, application crashes, security vulnerabilities, malware, etc. Scrutinize distribution packages before installing.

Install the latest version of rich.

NOTE: Pip installs the rich module and all of its dependencies.

Copy code
python3 -m pip install rich


Verify the module has been installed.

NOTE: Notice the rich module isn't the only module installed. Pip installs the dependencies of each required module.

Copy code
python3 -m pip list

The show command displays details about an installed package.

Review the details of the newly installed rich module.

Copy code
python3 -m pip show rich


With the rich module installed, running the cloudacademy/playground.py code file will now produce the desired results.

Run the cloudacademy/playground.py code file.

Copy code
python3 cloudacademy/playground.py


The uninstall command removes the specified package. By default the uninstall command prompts for confirmation.

Uninstall the rich module.

Enter Y when prompted.
Copy code
python3 -m pip uninstall rich



To remove a package without being prompted use either the -y short flag or the --yes flag.

Examples:

Copy code
python3 -m pip uninstall rich -y
python3 -m pip uninstall rich --yes
Multiple packages may require the same dependent module. Pip doesn't uninstall a module's dependencies in order to prevent the accidental removal of still required modules

Verify the module has been removed.

NOTE: Notice only rich was removed and not its dependencies.

Copy code
python3 -m pip list


Defined in 
PEP 508
, opens in a new tab, pip includes a syntax for specifying which package, version, and optional dependencies should be installed. This syntax is referred to as requirement specifiers.

The following command uses the == operator to specify the exact package version.

Install a specific version of the rich module.

Copy code
python3 -m pip install rich==12.3.0


Review the details of the newly installed module.

NOTE: Notice the installed version is now v12.3.0.

