from enum import Enum

class OfficeUpdateChannel(Enum):
    None_escaped = "none",
    Current = "current",
    Deferred = "deferred",
    FirstReleaseCurrent = "firstReleaseCurrent",
    FirstReleaseDeferred = "firstReleaseDeferred",
    MonthlyEnterprise = "monthlyEnterprise",

