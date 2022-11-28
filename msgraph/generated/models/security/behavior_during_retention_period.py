from enum import Enum

class BehaviorDuringRetentionPeriod(Enum):
    DoNotRetain = "doNotRetain",
    Retain = "retain",
    RetainAsRecord = "retainAsRecord",
    RetainAsRegulatoryRecord = "retainAsRegulatoryRecord",
    UnknownFutureValue = "unknownFutureValue",

