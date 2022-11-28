from enum import Enum

class DelegatedPrivilegeStatus(Enum):
    None_escaped = "none",
    DelegatedAdminPrivileges = "delegatedAdminPrivileges",
    UnknownFutureValue = "unknownFutureValue",
    GranularDelegatedAdminPrivileges = "granularDelegatedAdminPrivileges",
    DelegatedAndGranularDelegetedAdminPrivileges = "delegatedAndGranularDelegetedAdminPrivileges",

