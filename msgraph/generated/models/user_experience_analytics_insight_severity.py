from enum import Enum

class UserExperienceAnalyticsInsightSeverity(str, Enum):
    None_ = "none",
    Informational = "informational",
    Warning = "warning",
    Error = "error",

