# NextGen Coding Bootcamp: Session 07

## :wave: Managing Environments and Configuring Programs

In this workshop we will explore how to setup and configure Python environments to improve the reproducibility of your code. We will then dive into configuration files and how to use these to configure more complex systems. 

## :wrench: Setting up your Environment

This workshop **requires** you to be running a Python IDE such as VSCode or PyCharm. First, we will explore a couple of different methods for creating Python virtual environments

### Creating an environment using `pip`

`pip` is a Python package manager that allows us to install Python packages into a given Python environment. We can create an environment on Linux by running the following commands, however your system needs to have the Python language installed on your machine to be able to use it.

```Bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

We create an environment the same way on Windows Command Line, however we use `.venv/Scripts/activate` to activate the environment.

```Bash
python -m venv .venv
.venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

There can be some different variants of the command to activate depending on WSL, Git Bash, Command Prompt, PowerShell, etc. but the same structure remains.


### Creating an environment using `conda`

Conda is a little bit different and is a system package manager, it allows us to install system packages such as Python itself. This allows us to be a bit more specific in our definitions, essentailly enabling us to select a Python version too, however it can be more nuanced than this. 

```Bash
conda update -n base -c defaults conda
conda env create -f environment.yaml
conda activate .venv
```

To remove a conda environment use the following command.

```Bash
conda remove -n .venv --all
```


## Create a .env file for storing environment variables

Once you've loaded your virtual Python environment we're going to run the following commands in the command line.

```Bash
python # to enter python
```

Then we're going to get the current directory of the project.

```Python
import os
os.getcwd()
```

We're going to copy the output of this and create a file called `.env` in the root directory of the project and paste the directory into there in the format shown in `example.env`.
