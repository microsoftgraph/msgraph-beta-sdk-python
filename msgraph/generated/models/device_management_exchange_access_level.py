from enum import Enum

class DeviceManagementExchangeAccessLevel(Enum):
    # No device access rule has been configured in Exchange.
    None_escaped = "none",
    # Allow the device access to Exchange.
    Allow = "allow",
    # Block the device from accessing Exchange.
    Block = "block",
    # Quarantine the device in Exchange.
    Quarantine = "quarantine",

