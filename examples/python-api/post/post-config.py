from datetime import datetime
from pathlib import Path
from pprint import pprint as pp

from pyaviso import NotificationManager, user_config

# Get the path of the current script
script_path = Path(__file__).resolve()
# Get the root path of the repository
repository_root = str(script_path.parents[3])

# Constants
START_DATE = datetime(1999, 12, 12)  # Start date for the notification listener
LISTENER_EVENT = "mars"  # Event for the listener, options are mars and dissemination
TRIGGER_TYPE = "post"  # Type of trigger for the listener
REQUEST = {
    "class": "od",
    "expver": 1,
    "stream": "enfo",
    "step": [1, 2, 3],
    "domain": "g",
}  # Request configuration for the listener
CONFIG = {
    "notification_engine": {
        "host": "aviso.ecmwf.int",
        "port": 443,
        "https": True,
    },
    "configuration_engine": {"host": "aviso.ecmwf.int", "port": 443, "https": True},
    "schema_parser": "ecmwf",
    "remote_schema": True,
    "auth_type": "ecmwf",
    "username_file": repository_root / Path(".username"),
    "key_file": repository_root / Path(".key"),
}  # manually defined configuration


def create_listener():
    """
    Creates and returns a listener configuration.
    """

    trigger = {
        "type": TRIGGER_TYPE,
        "protocol": {"type": "cloudevents_http", "url": "http://httpbin.org/post"},
    }  # Define the trigger for the listener
    # Return the complete listener configuration
    return {"event": LISTENER_EVENT, "request": REQUEST, "triggers": [trigger]}


def main():
    try:
        listener = create_listener()  # Create listener configuration
        listeners_config = {"listeners": [listener]}  # Define listeners configuration
        config = user_config.UserConfig(**CONFIG)
        print("loaded config:")
        pp(CONFIG)
        nm = NotificationManager()  # Initialize the NotificationManager
        nm.listen(
            listeners=listeners_config, from_date=START_DATE, config=config
        )  # Start listening
    except Exception as e:
        print(f"Failed to initialize the Notification Manager: {e}")


if __name__ == "__main__":
    main()
