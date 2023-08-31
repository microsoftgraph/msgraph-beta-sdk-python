from enum import Enum

class CallDisposition(str, Enum):
    Default = "default",
    SimultaneousRing = "simultaneousRing",
    Forward = "forward",

