from enum import Enum

class EnrollmentTimeDeviceMembershipTargetType(str, Enum):
    # Indicates the device membership target specified refer to static Entra Security Groups.
    StaticSecurityGroup = "staticSecurityGroup",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

