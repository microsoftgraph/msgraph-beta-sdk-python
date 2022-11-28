from enum import Enum

class WindowsAutopilotDeviceRemediationState(Enum):
    # Unknown status.
    Unknown = "unknown",
    # No hardware change has been detected.
    NoRemediationRequired = "noRemediationRequired",
    # Hardware change detected on client. Additional remediation is required.
    AutomaticRemediationRequired = "automaticRemediationRequired",
    # Hardware change detected on client that could not resolved automatically. Additional remediation is required.
    ManualRemediationRequired = "manualRemediationRequired",
    # Marks the end of known enum values, and allows for additional values in the future.
    UnknownFutureValue = "unknownFutureValue",

