from enum import Enum

class UsageStatus(str, Enum):
    FrequentlyUsed = "frequentlyUsed",
    RarelyUsed = "rarelyUsed",
    UnknownFutureValue = "unknownFutureValue",

