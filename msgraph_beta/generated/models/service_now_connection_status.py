from enum import Enum

class ServiceNowConnectionStatus(str, Enum):
    # Tenant has disabled the connection
    Disabled = "disabled",
    # Tenant has enabled the connection
    Enabled = "enabled",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

