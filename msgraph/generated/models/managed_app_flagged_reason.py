from enum import Enum

class ManagedAppFlaggedReason(Enum):
    # No issue.
    None_escaped = "none",
    # The app registration is running on a rooted/unlocked device.
    RootedDevice = "rootedDevice",
    # The app registration is running on an Android device on which the bootloader is unlocked.
    AndroidBootloaderUnlocked = "androidBootloaderUnlocked",
    # The app registration is running on an Android device on which the factory ROM has been modified.
    AndroidFactoryRomModified = "androidFactoryRomModified",

