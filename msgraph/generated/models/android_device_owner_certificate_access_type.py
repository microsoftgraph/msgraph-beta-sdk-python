from enum import Enum

class AndroidDeviceOwnerCertificateAccessType(Enum):
    # Require user approval for all apps
    UserApproval = "userApproval",
    # Pre-grant certificate access for specific apps (require user approval for other apps).
    SpecificApps = "specificApps",
    # Unknown future value for evolvable enum patterns.
    UnknownFutureValue = "unknownFutureValue",

