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
.venv/Scripts/activate # you might also need to use .venv\\Scripts\\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

There can be some different variants of the command to activate depending on WSL, Git Bash, Command Prompt, PowerShell, etc. but the same structure remains (you can see these different options in the .venv/Scripts folder).


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

Please create a `.env` file by running the following Python script from the projects root directory.

```Bash
python setup.py
```

This will create a `.env` file with the key PROJECT_ROOT=... that we will use to ensure Python knows where to look for `src` files and construct paths relative to the projects root directory. You can see an example of this in the `example.env` file.
