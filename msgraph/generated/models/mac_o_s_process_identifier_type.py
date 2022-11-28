from enum import Enum

class MacOSProcessIdentifierType(Enum):
    # Indicates an app with a bundle ID.
    BundleID = "bundleID",
    # Indicates a file path for a process.
    Path = "path",

