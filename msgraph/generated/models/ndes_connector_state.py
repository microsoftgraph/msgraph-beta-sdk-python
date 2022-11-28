from enum import Enum

class NdesConnectorState(Enum):
    # State not available yet for this connector.
    None_escaped = "none",
    # Ndes connector has connected recently
    Active = "active",
    # No recent activity for the Ndes connector
    Inactive = "inactive",

