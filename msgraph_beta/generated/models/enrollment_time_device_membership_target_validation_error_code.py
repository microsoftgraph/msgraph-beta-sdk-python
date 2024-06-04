from enum import Enum

class EnrollmentTimeDeviceMembershipTargetValidationErrorCode(str, Enum):
    # Default. Indicates the status of device membership target is not specified. Do not use.
    Unknown = "unknown",
    # Indicates device membership target cannot be found.
    SecurityGroupNotFound = "securityGroupNotFound",
    # Indicates device membership target is not a security group.
    NotSecurityGroup = "notSecurityGroup",
    # Indicates device membership target which is security group but not a static one.
    NotStaticSecurityGroup = "notStaticSecurityGroup",
    # Indicates required first party app not the owner of that device membership target.
    FirstPartyAppNotAnOwner = "firstPartyAppNotAnOwner",
    # Indicates that device membership target of type security group is not in the RBAC scope of the caller.
    SecurityGroupNotInCallerScope = "securityGroupNotInCallerScope",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

