from enum import Enum

class AndroidManagedAppSafetyNetEvaluationType(Enum):
    # Require basic evaluation
    Basic = "basic",
    # Require hardware backed evaluation
    HardwareBacked = "hardwareBacked",

