"""Constants for Eufy RoboVac 11c."""
# Base component constants
NAME = "Eufy RoboVac 11c"
DOMAIN = "eufy_robovac_11c"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "1.0.0"

ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
ISSUE_URL = "https://github.com/jonjomckay/eufy-robovac-11c/issues"

# Icons
ICON = "mdi:format-quote-close"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
PLATFORMS = [BINARY_SENSOR, SENSOR, SWITCH]


# Configuration and options
# CONF_ENABLED = "enabled"
# CONF_USERNAME = "username"
# CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = NAME


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
