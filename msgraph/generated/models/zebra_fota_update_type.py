from enum import Enum

class ZebraFotaUpdateType(str, Enum):
    # Custom update where the user selects specific BSP, OS version, and patch number to update to.
    Custom = "custom",
    # The latest released update becomes the target OS. Latest may update the device to a new Android version.
    Latest = "latest",
    # The device always looks for the latest package available in the repo and tries to update whenever a new package is available. This continues until the admin cancels the auto update.
    Auto = "auto",
    # Unknown future enum value.
    UnknownFutureValue = "unknownFutureValue",

