from enum import Enum

class ScheduleRequestActions(Enum):
    AdminAssign = "adminAssign",
    AdminUpdate = "adminUpdate",
    AdminRemove = "adminRemove",
    SelfActivate = "selfActivate",
    SelfDeactivate = "selfDeactivate",
    AdminExtend = "adminExtend",
    AdminRenew = "adminRenew",
    SelfExtend = "selfExtend",
    SelfRenew = "selfRenew",
    UnknownFutureValue = "unknownFutureValue",

