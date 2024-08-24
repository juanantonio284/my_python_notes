# Creation of virtual environments with `venv`

## TLDR

```Bash

# INSTALL venv module (only do this once)
sudo apt install python3-venv

# CREATE A NEW VIRTUAL ENVIRONMENT
python3 -m venv ~/.virtualenvs # Create a new virtual environment
# in this example, the venv will be made in a hidden folder (.) named "virtualenvs"
# this venv is around 17 MB in size before any packages are installed

# ACTIVATE a previously created virtual environment in the terminal
source ~/.virtualenvs/bin/activate # Activate the virtual environment in the terminal
# (This sources the "activate" script in the bin folder)
# The terminal will now show something like:    (.virtualenvs) username@username:~$

# INSTALL NEEDED PYTHON PACKAGES 
# e.g.
python3 -m pip install django

```

## `venv`

[original_page][venv]

[venv]: https://docs.python.org/3/library/venv.html#module-venv

The `venv` module supports creating lightweight "virtual environments", each with their own
independent set of Python packages installed in their site directories. A virtual environment is
created on top of an existing Python installation, known as the virtual environment's "base"
Python, and **may optionally be isolated from the packages in the base environment**, so only those
explicitly installed in the virtual environment are available.

<!-- *** did we isolate from the packages in the base environment? -->

When used from within a virtual environment, common installation tools such as `pip` will install
Python packages into a virtual environment without needing to be told to do so explicitly.

A virtual environment is:

* Used to contain a specific Python interpreter and software libraries and binaries which are needed
  to support a project (library or application). These (i.e. the Python interpreter, the libraries,
  and the binaries) are by default isolated from software in other virtual environments, and from
  other Python interpreters and libraries installed in the operating system.

* Contained in a directory, conventionally either named `venv` or `.venv` in the project directory.
  A virtual environment can also be under a container directory for lots of virtual environments,
  such as `~/.virtualenvs`.

* Not checked into source control systems such as Git.

* Considered disposable—it should be simple to delete and recreate it from scratch—so you don't
  place any project code in the environment

* Not considered as movable or copyable – you just recreate the same environment in the target
  location.

**Install `venv` module**

```Bash

# Install venv module
sudo apt install python3-venv # only do this once

```

### Creating a virtual environment

```Bash

# Create virtual environment in the local home folder
python3 -m venv ~/.virtualenvs # do this whenever you want to create a new one

```

Running this command:

* creates the target directory (creating any parent directories that don't exist already) 

* places a `pyvenv.cfg` file in it with a home key pointing to the Python installation from which
  the command was run (a common name for the target directory is `.venv`).

* creates a bin subdirectory containing a copy/symlink of the Python binary/binaries (as appropriate
  for the platform or arguments used at environment creation time)

* creates an (initially empty) `lib/pythonX.Y/site-packages` subdirectory (if an existing directory
  is specified, it will be re-used)

**Options**

`venv -h`, will show the available options:

```

usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear]
            [--upgrade] [--without-pip] [--prompt PROMPT] [--upgrade-deps]
            ENV_DIR [ENV_DIR ...]

Creates virtual Python environments in one or more target directories.

positional arguments:
  ENV_DIR               A directory to create the environment in.

optional arguments:
  -h, --help            show this help message and exit
  --system-site-packages
                        Give the virtual environment access to the system
                        site-packages dir.
  --symlinks            Try to use symlinks rather than copies, when symlinks
                        are not the default for the platform.
  --copies              Try to use copies rather than symlinks, even when
                        symlinks are the default for the platform.
  --clear               Delete the contents of the environment directory if it
                        already exists, before environment creation.
  --upgrade             Upgrade the environment directory to use this version
                        of Python, assuming Python has been upgraded in-place.
  --without-pip         Skips installing or upgrading pip in the virtual
                        environment (pip is bootstrapped by default)
  --prompt PROMPT       Provides an alternative prompt prefix for this
                        environment.
  --upgrade-deps        Upgrade core dependencies (pip) to the
                        latest version in PyPI

Once an environment has been created, you may wish to activate it, e.g. by
sourcing an activate script in its bin directory.

```

### How `venvs` work

A virtual environment may be "activated" using a script in its binary directory. This will prepend
that directory to your PATH, so that running python will invoke the environment's Python
interpreter and you can run installed scripts without having to use their full path. 
[The invocation of the activation script is platform-specific][table_1]

[table_1]: https://docs.python.org/3/library/venv.html#how-venvs-work

For POSIX platform on bash/zsh, the command to activate virtual environment is
`$ source <venv>/bin/activate`  
(`<venv>` must be replaced by the path to the directory containing the virtual environment.)

```Bash

# Start the virtual environment in the terminal
source ~/.virtualenvs/bin/activate

```

You don't specifically need to activate a virtual environment, as you can just specify the full path
to that environment's Python interpreter when invoking Python. Furthermore, all scripts installed
in the environment should be runnable without activating it. (In order to achieve this, scripts
installed into virtual environments have a "shebang" line which points to the environment's Python
interpreter, i.e. `#!/<path-to-venv>/bin/python`. This means that the script will run with that
interpreter regardless of the value of PATH.)

When a virtual environment has been activated, the VIRTUAL_ENV environment variable is set to the
path of the environment. Since explicitly activating a virtual environment is not required to use
it, VIRTUAL_ENV cannot be relied upon to determine whether a virtual environment is being used.

**Warning**

Because scripts installed in environments should not expect the environment to be activated, their
shebang lines contain the absolute paths to their environment's interpreters. Because of this,
environments are inherently non-portable, in the general case. 

You should always have a simple means of recreating an environment (for example, if you have a
requirements file `requirements.txt`, you can invoke `pip install -r requirements.txt` using the
environment's `pip` to install all of the packages needed by the environment). 

If for any reason you need to move the environment to a new location, you should recreate it at the
desired location and delete the one at the old location. If you move an environment because you
moved a parent directory of it, you should recreate the environment in its new location. Otherwise,
software installed into the environment may not work as expected. 

### Change the python interpreter that loads in the vscode terminal

https://docs.posit.co/ide/server-pro/user/vs-code/guide/python-environments.html#set-the-default-project-interpreter

Now you can configure VS Code always to use this virtual environment when working on this project.
Open the Command Palette and type "Python: Select Interpreter". VS Code should automatically
recommend the virtual environment you just created. Select it using the arrow keys and press enter.
If VS Code does not automatically detect or recommend the new virtual environment, you can manually
enter the path: "`./venv/bin/python`".

Alternatively, you can select the default project interpreter by clicking on the Python section of
the Status Bar located at the bottom right of the window.
