## Overview

In this directory, you will find two key configuration files for each folder:

- `listen-diss.yaml`: For listening to dissemination events.
- `listen-mars.yaml`: For listening to Mars notifications.

These files are designed to help you set up listeners for different types of notifications in **aviso**.

## Dissemination Event Listener (`listen-diss.yaml`)

The `listen-diss.yaml` file is configured to listen for dissemination events. The request section of this file specifies the criteria for the dissemination events you want to trigger. It consists of various fields that you can use as filters. 

### Key Points:

- **Customization**: The `destination` field is mandatory for dissemination events. It should correspond to one or more destinations linked to your ECMWF account. Ensure you customize this field in `listen-diss.yaml` before initiating the listener.
- **Filtering**: Only notifications that comply with all defined fields in the request will trigger the command.
- **Setup**: Remember to populate the `.key` and `.username` files in the root folder and source `env.sh` before running.

## Mars Notifications Listener (`listen-mars.yaml`)

For listening to Mars notifications, use the `listen-mars.yaml` file. Unlike the dissemination listener, this configuration does not include a `destination` field.

### Usage:

To start listening for Mars notifications:

1. Ensure that `.key` and `.username` files are filled with your credentials and that `env.sh` has been sourced.
2. Execute the following command:
   ```bash
   aviso listen listen-mars.yaml
   ```

### Important Note

- **Initial Notification Search Behavior**: When **aviso** is launched for the first time, it searches through all available notifications that meet the criteria specified in the request. In subsequent runs, **aviso** intelligently resumes from the last processed notification.
- **Retrieving Historical Notifications**: To extend the search to older notifications, the `--from` flag proves instrumental. Example usage:
  ```bash
  aviso listen listen-mars.yaml --from 2020-01-20T00:00:00.0Z
  ```
This parameter directs aviso to initiate the search from the specified date, allowing for retrospective monitoring of notifications.

### Key Considerations

- **Understanding the `--from` Flag**: The date you use with the `--from` flag refers only to when the notification was originally sent, not to any 'date' mentioned in your request settings. It's used to specify the starting point for searching old notifications.
- **Notification Storage Limit**: **aviso** stores notifications for only the last 15 days. So, even if you set an earlier date with the `--from` flag, you can only access notifications from the past 15 days.


### Trigger Execution
Upon detecting new notifications, aviso will execute the command_script.sh bash script, which is also located in this directory. This script defines the actions to be taken when a notification is received.