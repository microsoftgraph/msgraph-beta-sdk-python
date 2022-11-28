from enum import Enum

class IncludedUserRoles(Enum):
    All = "all",
    PrivilegedAdmin = "privilegedAdmin",
    Admin = "admin",
    User = "user",
    UnknownFutureValue = "unknownFutureValue",

