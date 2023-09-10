# Philips rfx9600 Service for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

This repo contains a Home Assistant integration for Philips RFX9600.  The integration currently allows you to control relays.

## Installation

The preferred installation approach is via Home Assistant Community Store - aka [HACS](https://hacs.xyz/).  The repo is installable as a [Custom Repo](https://hacs.xyz/docs/faq/custom_repositories) via HACS.

If you want to download the integration manually, create a new folder called rfx9600_service under your custom_components folder in your config folder.  If the custom_components folder doesn't exist, create it first.  Once created, download the 3 files from the [github repo](https://github.com/peteS-UK/rfx9600Service/tree/main/custom_components/rfx9600_service) into this rfx9600_service folder.

Once downloaded either via HACS or manually, restart your Home Assistant server.

## Configuration

To enable the integration, add the following line to your configuration.yaml file, typically in your /config folder.

```yaml
rfx9600_service:
```

Once updated, restart your Home Assistant server again to enable the integration.

