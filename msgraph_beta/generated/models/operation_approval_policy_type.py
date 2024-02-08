from enum import Enum

class OperationApprovalPolicyType(str, Enum):
    # Default. Indicates that the configured policy type is unknown. This property is not allowed on an OperationApprovalRequest unless the PolicySet contains a different OperationApprovalPolicyType.
    Unknown = "unknown",
    # Indicates that the configured policy type is for a Device Action.
    DeviceAction = "deviceAction",
    # Indicates that the configured policy type is for a Device Wipe Action.
    DeviceWipe = "deviceWipe",
    # Indicates that the configured policy type is for a Device Retire Action.
    DeviceRetire = "deviceRetire",
    # Indicates that the configured policy type is for a Retire Non-Compliant Devices Action.
    DeviceRetireNonCompliant = "deviceRetireNonCompliant",
    # Indicates that the configured policy type is for a Device Delete Action.
    DeviceDelete = "deviceDelete",
    # Indicates that the configured policy type is for a Device Lock Action.
    DeviceLock = "deviceLock",
    # Indicates that the configured policy type is for a Device Erase Action.
    DeviceErase = "deviceErase",
    # Indicates that the configured policy type is for a Device Disable Activation Lock Action.
    DeviceDisableActivationLock = "deviceDisableActivationLock",
    # Indicates that the configured policy type is for a Windows Enrollment.
    WindowsEnrollment = "windowsEnrollment",
    # Indicates that the configured policy type is for a Compliance Policy.
    CompliancePolicy = "compliancePolicy",
    # Indicates that the configured policy type is for a Configuration Policy.
    ConfigurationPolicy = "configurationPolicy",
    # Indicates that the configured policy type is for an App Protection Policy.
    AppProtectionPolicy = "appProtectionPolicy",
    # Indicates that the configured policy type is for a Policy Set.
    PolicySet = "policySet",
    # Indicates that the configured policy type is for a Filter.
    Filter = "filter",
    # Indicates that the configured policy type is for an Endpoint Security Policy.
    EndpointSecurityPolicy = "endpointSecurityPolicy",
    # Indicates that the configured policy type is an application type, such as mobile apps or built-in apps.
    App = "app",
    # Indicates that the configured policy type is a script type, such as Powershell scripts or remediation scripts.
    Script = "script",
    # Indicates that the configured policy type is for a Role.
    Role = "role",
    # Indicates that the configured policy type is for a Device Reset Passcode Action.
    DeviceResetPasscode = "deviceResetPasscode",
    # Indicates that the configured policy type is for a Custom Organizational Message.
    CustomOrganizationalMessage = "customOrganizationalMessage",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

