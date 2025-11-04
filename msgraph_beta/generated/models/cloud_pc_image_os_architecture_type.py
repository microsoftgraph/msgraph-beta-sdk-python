from enum import Enum

class CloudPcImageOsArchitectureType(str, Enum):
    X64 = "x64",
    Arm64 = "arm64",
    UnknownFutureValue = "unknownFutureValue",

