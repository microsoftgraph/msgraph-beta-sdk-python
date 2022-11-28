from enum import Enum

class CloudPcAuditActivityOperationType(Enum):
    Create = "create",
    Delete = "delete",
    Patch = "patch",
    Other = "other",

