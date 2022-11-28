from enum import Enum

class RoutingPolicy(Enum):
    None_escaped = "none",
    NoMissedCall = "noMissedCall",
    DisableForwardingExceptPhone = "disableForwardingExceptPhone",
    DisableForwarding = "disableForwarding",
    PreferSkypeForBusiness = "preferSkypeForBusiness",
    UnknownFutureValue = "unknownFutureValue",

