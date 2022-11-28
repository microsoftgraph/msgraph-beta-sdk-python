from enum import Enum

class DeviceManagementConfigurationTechnologies(Enum):
    # Setting cannot be deployed through any channel
    None_escaped = "none",
    # Setting can be deployed through the MDM channel
    Mdm = "mdm",
    # Setting can be deployed through the Windows10XManagement channel
    Windows10XManagement = "windows10XManagement",
    # Setting can be deployed through the ConfigManager channel
    ConfigManager = "configManager",
    # Setting can be deployed through the AppleRemoteManagement channel
    AppleRemoteManagement = "appleRemoteManagement",
    # Setting can be deployed through the SENSE agent channel
    MicrosoftSense = "microsoftSense",
    # Setting can be deployed through the Exchange Online agent channel
    ExchangeOnline = "exchangeOnline",
    # Setting can be deployed through the Linux Mdm channel
    LinuxMdm = "linuxMdm",
    # Setting can be deployed through device enrollment.
    Enrollment = "enrollment",
    # Setting can be deployed using the Endpoint privilege management channel
    EndpointPrivilegeManagement = "endpointPrivilegeManagement",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

