import os
from datetime import datetime

from pyaviso import NotificationManager

# Constants
START_DATE = datetime(1999, 12, 12)  # Start date for the notification listener
LISTENER_EVENT = "mars"  # Event for the listener, options are mars and dissemination
TRIGGER_TYPE = "echo"  # Type of trigger for the listener
REQUEST = {
    "class": "od",
    "expver": 1,
    "stream": "enfo",
    "step": [1, 2, 3],
    "domain": "g",
}  # Request configuration for the listener


def check_env():
    """
    Checks if necessary env.sh is sourced before running this script.
    """
    if (
        "AVISO_CONFIGURATION_HOST" not in os.environ
        or "AVISO_NOTIFICATION_HOST" not in os.environ
    ):
        print("env.sh should be sourced before running this script")
        print("env.sh can be found in the root folder of this repository.")
        exit(1)


def create_listener():
    """
    Creates and returns a listener configuration.
    """

    trigger = {"type": TRIGGER_TYPE}  # Define the trigger for the listener
    # Return the complete listener configuration
    return {"event": LISTENER_EVENT, "request": REQUEST, "triggers": [trigger]}


def main():
    check_env()  # Check if env.sh is sourced

    try:
        listener = create_listener()  # Create listener configuration
        listeners_config = {"listeners": [listener]}  # Define listeners configuration

        nm = NotificationManager()  # Initialize the NotificationManager
        nm.listen(listeners=listeners_config, from_date=START_DATE)  # Start listening
    except Exception as e:
        print(f"Failed to initialize the Notification Manager: {e}")


if __name__ == "__main__":
    main()
