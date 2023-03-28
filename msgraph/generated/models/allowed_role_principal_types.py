from enum import Enum

class AllowedRolePrincipalTypes(Enum):
    User = "user",
    ServicePrincipal = "servicePrincipal",
    Group = "group",
    UnknownFutureValue = "unknownFutureValue",

