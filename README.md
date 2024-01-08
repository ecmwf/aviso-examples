
# aviso-examples
This repository hosts a collection of example Python scripts and configuration files specifically designed for the **aviso** software. These examples are intended to illustrate how aviso can be effectively utilized with data distributed by the European Centre for Medium-Range Weather Forecasts (ECMWF).

## About Aviso

**aviso** is a software developed by ECMWF that allows the notification of **time-critical events** across HPC and Cloud systems in order to enable workflows among multiple domains.

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

## Folder Structure
In the examples folder at the root of this repository, you will find two subdirectories:

cli: Contains examples demonstrating how to use aviso via command-line interface (CLI).
python-api: Includes examples for running aviso using its Python API.

These examples are designed to provide a practical understanding of how to integrate and utilize aviso in various scenarios. In order to provide more comprehensive explanations of the examples, each folder contains a README file.