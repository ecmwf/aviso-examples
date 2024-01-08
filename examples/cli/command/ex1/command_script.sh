#!/bin/bash

# Function to show usage information
show_usage() {
    echo "Usage: $0 --json '{\"key\": \"value\"}'"
    echo "The --json flag is required and should be followed by a JSON string."
}

# Check if at least two arguments are supplied
if [ "$#" -ne 2 ]; then
    show_usage
    exit 1
fi

# Check if the first argument is the --json flag
if [ "$1" != "--json" ]; then
    show_usage
    exit 1
fi

# Assign the JSON string to a variable
json_string=$2

# Pretty print the JSON string
if ! jq . <<< "$json_string" > /dev/null 2>&1; then
    echo "Error: Invalid JSON string provided."
    exit 1
else
    echo "This message is produced by the command script."
    echo "Here is the content of the notification:"
    jq . <<< "$json_string"
fi
