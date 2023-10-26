from enum import Enum

class ActionSource(str, Enum):
    Manual = "manual",
    Automatic = "automatic",
    Recommended = "recommended",
    Default = "default",

