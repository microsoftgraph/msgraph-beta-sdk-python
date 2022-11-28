from enum import Enum

class DeviceGuardVirtualizationBasedSecurityHardwareRequirementState(Enum):
    # System meets hardware configuration requirements
    MeetHardwareRequirements = "meetHardwareRequirements",
    # Secure boot required
    SecureBootRequired = "secureBootRequired",
    # DMA protection required
    DmaProtectionRequired = "dmaProtectionRequired",
    # HyperV not supported for Guest VM
    HyperVNotSupportedForGuestVM = "hyperVNotSupportedForGuestVM",
    # HyperV feature is not available
    HyperVNotAvailable = "hyperVNotAvailable",

