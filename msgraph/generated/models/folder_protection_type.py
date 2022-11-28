from enum import Enum

class FolderProtectionType(Enum):
    # Device default value, no intent.
    UserDefined = "userDefined",
    # Block functionality.
    Enable = "enable",
    # Allow functionality but generate logs.
    AuditMode = "auditMode",
    # Block untrusted apps from writing to disk sectors.
    BlockDiskModification = "blockDiskModification",
    # Generate logs when untrusted apps write to disk sectors.
    AuditDiskModification = "auditDiskModification",

