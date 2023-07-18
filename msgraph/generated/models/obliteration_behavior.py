from enum import Enum

class ObliterationBehavior(str, Enum):
    # Default. If Erase All Content and Settings (EACS) preflight fails, the device responds to the server with an Error status and then attempts to erase itself. If EACS preflight succeeds but EACS fails, then the device attempts to erase itself.
    Default = "default",
    # If Erase All Content and Settings (EACS) preflight fails, the device responds to the server with an Error status and doesn’t attempt to erase itself. If EACS preflight succeeds but EACS fails, then the device doesn’t attempt to erase itself.
    DoNotObliterate = "doNotObliterate",
    # If Erase All Content and Settings (EACS) preflight fails, the device responds with an Acknowledged status and then attempts to erase itself. If EACS preflight succeeds but EACS fails, then the device attempts to erase itself.
    ObliterateWithWarning = "obliterateWithWarning",
    # The system doesn’t attempt Erase All Content and Settings (EACS). T2 and later devices always obliterate.
    Always = "always",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

