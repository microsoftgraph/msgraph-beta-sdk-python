from enum import Enum

class MobileAppDependencyType(Enum):
    # Indicates that the child app should be detected before installing the parent app.
    Detect = "detect",
    # Indicates that the child app should be installed before installing the parent app.
    AutoInstall = "autoInstall",

