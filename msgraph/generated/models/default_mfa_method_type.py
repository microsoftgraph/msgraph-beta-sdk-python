from enum import Enum

class DefaultMfaMethodType(Enum):
    None_escaped = "none",
    MobilePhone = "mobilePhone",
    AlternateMobilePhone = "alternateMobilePhone",
    OfficePhone = "officePhone",
    MicrosoftAuthenticatorPush = "microsoftAuthenticatorPush",
    SoftwareOneTimePasscode = "softwareOneTimePasscode",
    UnknownFutureValue = "unknownFutureValue",

