## Overview

This directory contains two configuration files designed to set up listeners for two different types of notifications in **aviso**:

- `listen-diss.yaml`: For listening to dissemination events.
- `listen-mars.yaml`: For listening to Mars notifications.

The Echo trigger is designed to demonstrate a straightforward usage of **aviso**, where incoming notifications are simply printed to the console.

## Configuration and Usage

### Dissemination Event Listener (`listen-diss.yaml`)

The `listen-diss.yaml` is set up to listen for dissemination events. Customize the `destination` field to match destinations linked to your ECMWF account. This file allows you to specify various filter criteria to target specific dissemination events.

### Mars Notifications Listener (`listen-mars.yaml`)

The `listen-mars.yaml` file is configured for listening to Mars notifications. This setup does not require a `destination` field and is ready to use as provided.

### Steps to Run the Echo Trigger:

1. Ensure that `.key` and `.username` files in the root folder are populated with your credentials.
2. Source the `env.sh` file to set up the environment.
3. To start listening for notifications, execute the command:
   ```bash
   aviso listen [configuration-file.yaml]
   ```
Replace [configuration-file.yaml] with either listen-diss.yaml or listen-mars.yaml based on the type of notifications you want to listen to.

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

### Echo Functionality
When a new notification is detected, the Echo trigger will simply print the notification details to your console. This immediate feedback is useful for testing and understanding how aviso notifications are received and formatted.
