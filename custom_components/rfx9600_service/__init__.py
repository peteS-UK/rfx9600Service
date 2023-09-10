"""Example of a custom component exposing a service."""
from __future__ import annotations

import logging
import socket


from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.typing import ConfigType

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "rfx9600_service"
_LOGGER = logging.getLogger(__name__)


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the sync service example component."""

    def my_service(call: ServiceCall) -> None:
        """My first service."""
        _LOGGER.debug('Received data %s', call.data)

        rfx9600Ip = call.data.get("rfx9600Ip")

        rfx9600Action = call.data.get("rfx9600Action")

        rfx9600Relay = call.data.get("rfx9600Relay")

        rfx9600Port = 65442  # The port used by the server

        if rfx9600Action == "off" and rfx9600Relay == 1:
            command = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x63\x00\x00\x06\x00\x00\x00\x00"
        elif rfx9600Action == "on" and rfx9600Relay == 1:
            command = b"\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x63\x00\x00\x06\x00\x01\x00\x00"
        elif rfx9600Action == "off" and rfx9600Relay == 2:
            command = b"\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x63\x00\x00\x06\x01\x00\x00\x00"
        elif rfx9600Action == "on" and rfx9600Relay == 2:
            command = b"\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x63\x00\x00\x06\x01\x01\x00\x00"
        elif rfx9600Action == "off" and rfx9600Relay == 3:
            command = b"\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x63\x00\x00\x06\x02\x00\x00\x00"
        elif rfx9600Action == "on" and rfx9600Relay == 3:
            command = b"\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x63\x00\x00\x06\x02\x01\x00\x00"
        elif rfx9600Action == "off" and rfx9600Relay == 4:
            command = b"\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x63\x00\x00\x06\x03\x00\x00\x00"
        elif rfx9600Action == "on" and rfx9600Relay == 4:
            command = b"\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x63\x00\x00\x06\x03\x01\x00\x00"
        elif rfx9600Action == "toggle" and rfx9600Relay == 1:
            command = b"\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x64\x00\x00\x05\x00\x00\x00\x00"
        elif rfx9600Action == "toggle" and rfx9600Relay == 2:
            command = b"\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x64\x00\x00\x05\x01\x00\x00\x00"
        elif rfx9600Action == "toggle" and rfx9600Relay == 3:
            command = b"\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x64\x00\x00\x05\x02\x00\x00\x00"
        elif rfx9600Action == "toggle" and rfx9600Relay == 4:
            command = b"\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x64\x00\x00\x05\x03\x00\x00\x00"

        else:
            return False


        sock = socket.socket(socket.AF_INET, # Internet
                            socket.SOCK_DGRAM) # UDP

        try:
            sock.sendto(command, (rfx9600Ip, rfx9600Port))
        except (socket.error, socket.timeout):
            _LOGGER.debug  ("Send Failure.")
            sock.close()
            return False
        else:
            _LOGGER.debug  ("Message %s sent", command)
        finally:
            sock.close()


    # Register our service with Home Assistant.
    hass.services.register(DOMAIN, 'rfx9600', my_service)

    # Return boolean to indicate that initialization was successfully.
    return True
