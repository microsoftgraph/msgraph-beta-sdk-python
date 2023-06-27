from enum import Enum

class UsageAuthMethod(str, Enum):
    Email = "email",
    MobileSMS = "mobileSMS",
    MobileCall = "mobileCall",
    OfficePhone = "officePhone",
    SecurityQuestion = "securityQuestion",
    AppNotification = "appNotification",
    AppCode = "appCode",
    AlternateMobileCall = "alternateMobileCall",
    Fido = "fido",
    AppPassword = "appPassword",
    UnknownFutureValue = "unknownFutureValue",

