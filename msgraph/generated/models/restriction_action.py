from enum import Enum

class RestrictionAction(Enum):
    Warn = "warn",
    Audit = "audit",
    Block = "block",

