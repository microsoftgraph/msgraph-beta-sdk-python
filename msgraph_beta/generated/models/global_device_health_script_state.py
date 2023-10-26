from enum import Enum

class globalDeviceHealthScriptState(str, Enum):
    # Global device health scripts are not configured
    NotConfigured = "notConfigured",
    # Global device health scripts are configured but not fully enabled
    Pending = "pending",
    # Global device health scripts are enabled and ready to use
    Enabled = "enabled",

