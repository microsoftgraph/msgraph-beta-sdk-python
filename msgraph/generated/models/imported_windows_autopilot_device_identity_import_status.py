from enum import Enum

class ImportedWindowsAutopilotDeviceIdentityImportStatus(str, Enum):
    # Unknown status.
    Unknown = "unknown",
    # Pending status.
    Pending = "pending",
    # Partial status.
    Partial = "partial",
    # Complete status.
    Complete = "complete",
    # Error status.
    Error = "error",

