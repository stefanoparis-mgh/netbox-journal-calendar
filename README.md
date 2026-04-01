<div align="center">

  # NetBox Journal Calendar Plugin

  *A powerful visual calendar extension for NetBox Journal entries.*

  [![GitHub release](https://img.shields.io/github/v/release/stefanoparis-mgh/netbox-journal-calendar?include_prereleases&style=flat-square)](https://github.com/stefanoparis-mgh/netbox-journal-calendar/releases)
  [![License](https://img.shields.io/github/license/stefanoparis-mgh/netbox-journal-calendar?style=flat-square&color=blue)](LICENSE)
  [![Python](https://img.shields.io/badge/Python-3.13%2B-flat_square?logo=python&logoColor=white&color=blue)](https://www.python.org/)
  [![NetBox Compatibility](https://img.shields.io/badge/NetBox-4.5%2B-ff69b4?style=flat-square&logo=cisco&logoColor=white)](https://github.com/netbox-community/netbox)
  
  ---

  [Features](#-key-features) •
  [Installation](#-installation) •
  [Configuration](#-configuration) •
  [Screenshots](#-screenshots) •
  [Contributing](#-contributing)

</div>

<br>

## 📖 Introduction

**NetBox Journal Calendar** is a streamlined plugin designed to bring a comprehensive calendar view to the native NetBox journaling system. Instead of scrolling through text-heavy logs, this plugin transforms your existing Journal entries into an interactive, color-coded calendar interface.

It provides immediate visual context for network changes, maintenance windows, device installations, and other critical events registered within your infrastructure database.

## 🚀 Key Features

* 📅 **Full Calendar Integration:** View Journal entries in a standard Month layout.
* 📊 **Visual Categorization:** Events are automatically color-coded based on the Journal Entry type (*Success, Info, Warning, Danger*).
* 🔍 **Quick Peek View:** Click an event to instantly see the full note and a link to the associated NetBox object.
* 🛠️ **Native Experience:** Built to feel like a core part of the NetBox UI.
* 🧩 **Model Agnostic:** Works flawlessly with Journal entries from Devices, VMs, Circuits, IP Addresses, and all other supported models.

## 🛠️ Installation

### Step 1: Install the Package

Activate your NetBox virtual environment and install the plugin using pip:

```bash
# Navigate to NetBox directory
cd /opt/netbox
# Activate the virtual environment
source venv/bin/activate
# Install the plugin from GitHub
pip install git+[https://github.com/stefanoparis-mgh/netbox-journal-calendar](https://github.com/stefanoparis-mgh/netbox-journal-calendar)
```

### Step 2: Enable the Plugin

Edit your `configuration.py` (usually located at `/opt/netbox/netbox/netbox/configuration.py`) and add the plugin to the `PLUGINS` list:

```python
# configuration.py

PLUGINS = [
    'netbox_journal_calendar',
]
```

### Step 3: Run Migrations and Collect Static Files

The plugin requires database alignment and static JS/CSS files for the calendar rendering:

```bash
python3 netbox/manage.py migrate
python3 netbox/manage.py collectstatic --no-input
```

### Step 4: Restart NetBox Services

Restart the services to apply the changes:

```bash
sudo systemctl restart netbox netbox-rq
```

## ⚙️ Configuration

No specific configuration is required to get started. However, ensure that your users have the appropriate permissions to view **Journal Entries** within NetBox to see them on the calendar.

## 📸 Screenshots

### Calendar Dashboard
![Main View](https://raw.githubusercontent.com/stefanoparis-mgh/netbox-journal-calendar/main/docs/img/calendar_main.png)

### Event Details
![Detail View](https://raw.githubusercontent.com/stefanoparis-mgh/netbox-journal-calendar/main/docs/img/entry_detail.png)

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

**Developed with ❤️ by [stefanoparis-mgh](https://github.com/stefanoparis-mgh)**
