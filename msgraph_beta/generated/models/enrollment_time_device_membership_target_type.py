from enum import Enum

class EnrollmentTimeDeviceMembershipTargetType(str, Enum):
    # Default value. Do not use.
    Unknown = "unknown",
    # Indicates the device membership target specified refer to static Entra Security Groups.
    StaticSecurityGroup = "staticSecurityGroup",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

