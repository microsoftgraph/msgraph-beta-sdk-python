from enum import Enum

class AndroidDeviceOwnerEnrollmentProfileType(Enum):
    # Not configured; this value is ignored.
    NotConfigured = "notConfigured",
    # Dedicated device.
    DedicatedDevice = "dedicatedDevice",
    # Fully managed.
    FullyManaged = "fullyManaged",

