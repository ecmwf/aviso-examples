
# aviso-examples
This repository hosts a collection of example Python scripts and configuration files specifically designed for the **aviso** software. These examples are intended to illustrate how aviso can be effectively utilized with data distributed by the European Centre for Medium-Range Weather Forecasts (ECMWF).

## About Aviso

**aviso** is a software developed by ECMWF which provides **notification of time-critical data availability** events across HPC and Cloud systems in order to enable workflows among multiple domains.

It allows users to: 
* Define events that require notification
* Define triggers to be executed once a notification is received
* Send and receive notifications

This enables the creation of automatic workflows, timely triggered as events are notified.
The documentation can be found at https://pyaviso.readthedocs.io/

## Getting Started

### Prerequisites
Before you begin, ensure you have Python installed on your system. **aviso** is compatible with Python 3.6+.
### Installation
We recommend creating a virtual environment to manage the dependencies for your project. This helps in avoiding any conflicts with other Python packages you might have installed. Here's how you can do it:

```bash
# Install virtualenv if not already installed
pip  install  virtualenv
# Create a virtual environment
virtualenv  venv
# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source  venv/bin/activate
# Now, install aviso
pip  install  pyaviso
```

## Configuration

Before executing the example scripts in this repository, it is crucial to set up the necessary configuration files. This setup involves populating two files, `.key` and `.username`, and sourcing the `env.sh` file. All of these files are located in the root folder of the repository.

### Steps for Configuration

1. **Populate Credential Files**:
   - `.key` and `.username`: These files must be appropriately filled with your credentials.
   - To obtain these credentials, visit [ECMWF API Page](https://api.ecmwf.int/v1/key/).
   - Once you have your credentials, place the API key in the `.key` file and your email in the `.username` file.

2. **Source the Environment File**:
   - After setting up your credentials, you need to source the `env.sh` file to load the necessary environment variables.
   - You can do this by running the following command in the terminal from the root folder of the repository:
     ```bash
     source env.sh
     ```

## Folder Structure
In the examples folder at the root of this repository, you will find two subdirectories:

cli: Contains examples demonstrating how to use aviso via command-line interface (CLI).
python-api: Includes examples for running aviso using its Python API.

These examples are designed to provide a practical understanding of how to integrate and utilize aviso in various scenarios. In order to provide more comprehensive explanations of the examples, each folder contains a README file.

