from enum import Enum

class PlannerRelationshipUserRoles(Enum):
    DefaultRules = "defaultRules",
    GroupOwners = "groupOwners",
    GroupMembers = "groupMembers",
    TaskAssignees = "taskAssignees",
    Applications = "applications",
    UnknownFutureValue = "unknownFutureValue",

