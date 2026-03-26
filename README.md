<div align="center">

  <img src="https://raw.githubusercontent.com/netbox-community/netbox/develop/docs/netbox_logo.png" alt="NetBox Logo" width="120" height="120">

  # NetBox Journal Calendar Plugin

  *A powerful visual calendar extension for NetBox Journal entries.*

  [![GitHub release](https://img.shields.io/github/v/release/stefanoparis-mgh/netbox-journal-calendar?include_prereleases&style=flat-square)](https://github.com/stefanoparis-mgh/netbox-journal-calendar/releases)
  [![License](https://img.shields.io/github/license/stefanoparis-mgh/netbox-journal-calendar?style=flat-square&color=blue)](LICENSE)
  [![Python](https://img.shields.io/badge/Python-3.13%2B-flat_square?logo=python&logoColor=white&color=blue)](https://www.python.org/)
  [![NetBox Compatibility](https://img.shields.io/badge/NetBox-4.5%2B-ff69b4?style=flat-square&logo=cisco&logoColor=white)](https://github.com/netbox-community/netbox)
  
  ---

  [Features](#-key-features) •
  [Installation](#-installation) •
  [Configuration](#%EF%B8%8F-configuration) •
  [Screenshots](#-screenshots) •
  [Contributing](#-contributing)

</div>

<br>

## 📖 Introduction

**NetBox Journal Calendar** is a streamlined plugin designed to bring a comprehensive calendar view to the native NetBox journaling system. Instead of scrolling through text-heavy logs, this plugin transforms your existing Journal entries into an interactive, color-coded calendar interface.

It provides immediate visual context for network changes, maintanance windows, device installations, and other critical events registered within your infrastructure database.

## 🚀 Key Features

* 📅 **Full Calendar Integration:** View Journal entries in a standard Month, Week, or Day layout.
* 📊 **Visual Categorization:** Events are automatically color-coded based on the Journal Entry type (*Success, Info, Warning, Danger*).
* 🔍 **Quick Peek View:** Click an event to instantly see the full note and a link to the associated NetBox object.
* 🛠️ **Native Experience:** Built to feel like a core part of the NetBox UI.
* 🧩 **Model Agnostic:** Works flawlessly with Journal entries from Devices, VMs, Circuits, IP Addresses, and all other supported models.

## 🛠️ Installation

This plugin can be installed using git.

### Step 1: Install the Package

Activate your NetBox virtual environment and install the plugin.

```bash
source /opt/netbox/venv/bin/activate
pip install git+https://github.com/stefanoparis-mgh/netbox-journal-calendar
systemctl restart netbox netbox-rq
