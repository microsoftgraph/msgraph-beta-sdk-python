from enum import Enum

class AndroidManagedStoreLayoutType(str, Enum):
    # Default. Basic store layout where all approved apps are automatically visible in the Google Play Store.
    Basic = "basic",
    # Indicates a customized Google Play Store layout where only apps added to a specific collection in the Intune admin portal are visible in the Google Play Store on managed devices.
    Custom = "custom",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

