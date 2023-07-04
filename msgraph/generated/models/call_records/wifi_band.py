from enum import Enum

class WifiBand(str, Enum):
    Unknown = "unknown",
    Frequency24GHz = "frequency24GHz",
    Frequency50GHz = "frequency50GHz",
    Frequency60GHz = "frequency60GHz",
    UnknownFutureValue = "unknownFutureValue",

