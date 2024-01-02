from enum import Enum

class WiFiProxySetting(str, Enum):
    # No Proxy.
    None_ = "none",
    # Manual Proxy Settings via Address and Port.
    Manual = "manual",
    # Automatic Proxy Settings via URL.
    Automatic = "automatic",
    # Unknown future value for evolvable enum patterns.
    UnknownFutureValue = "unknownFutureValue",

