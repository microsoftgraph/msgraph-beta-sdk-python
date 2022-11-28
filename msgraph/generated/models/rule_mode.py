from enum import Enum

class RuleMode(Enum):
    Audit = "audit",
    AuditAndNotify = "auditAndNotify",
    Enforce = "enforce",
    PendingDeletion = "pendingDeletion",
    Test = "test",

