from enum import Enum

class VpnOnDemandRuleConnectionAction(Enum):
    # Connect.
    Connect = "connect",
    # Evaluate Connection.
    EvaluateConnection = "evaluateConnection",
    # Ignore.
    Ignore = "ignore",
    # Disconnect.
    Disconnect = "disconnect",

