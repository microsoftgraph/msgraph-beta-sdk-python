from enum import Enum

class DelegatedPrivilegeStatus(Enum):
    None_ = "none",
    DelegatedAdminPrivileges = "delegatedAdminPrivileges",
    UnknownFutureValue = "unknownFutureValue",
    GranularDelegatedAdminPrivileges = "granularDelegatedAdminPrivileges",
    DelegatedAndGranularDelegetedAdminPrivileges = "delegatedAndGranularDelegetedAdminPrivileges",

