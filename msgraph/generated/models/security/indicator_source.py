from enum import Enum

class IndicatorSource(str, Enum):
    MicrosoftDefenderThreatIntelligence = "microsoftDefenderThreatIntelligence",
    OpenSourceIntelligence = "openSourceIntelligence",
    Public = "public",
    UnknownFutureValue = "unknownFutureValue",

