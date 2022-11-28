from enum import Enum

class TeamworkSupportedClient(Enum):
    Unknown = "unknown",
    SkypeDefaultAndTeams = "skypeDefaultAndTeams",
    TeamsDefaultAndSkype = "teamsDefaultAndSkype",
    SkypeOnly = "skypeOnly",
    TeamsOnly = "teamsOnly",
    UnknownFutureValue = "unknownFutureValue",

