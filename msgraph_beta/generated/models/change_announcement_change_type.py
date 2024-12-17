from enum import Enum

class ChangeAnnouncementChangeType(str, Enum):
    BreakingChange = "breakingChange",
    Deprecation = "deprecation",
    EndOfSupport = "endOfSupport",
    FeatureChange = "featureChange",
    Other = "other",
    Retirement = "retirement",
    SecurityIncident = "securityIncident",
    UxChange = "uxChange",
    UnknownFutureValue = "unknownFutureValue",

