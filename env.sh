#!/bin/bash

export AVISO_NOTIFICATION_HOST="aviso.ecmwf.int"
export AVISO_NOTIFICATION_PORT=443
export AVISO_NOTIFICATION_HTTPS=True
export AVISO_CONFIGURATION_HOST="aviso.ecmwf.int"
export AVISO_CONFIGURATION_PORT=443
export AVISO_CONFIGURATION_HTTPS=True
export AVISO_SCHEMA_PARSER=ecmwf
export AVISO_REMOTE_SCHEMA=True
export AVISO_AUTH_TYPE=ecmwf

# Get the directory where this file is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Define variable relative to the script's directory
export AVISO_KEY_FILE="$DIR/.key"
export AVISO_USERNAME_FILE="$DIR/.username"