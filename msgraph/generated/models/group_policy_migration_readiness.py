from enum import Enum

class GroupPolicyMigrationReadiness(Enum):
    # No Intune coverage
    None_escaped = "none",
    # Partial Intune coverage
    Partial = "partial",
    # Complete Intune coverage
    Complete = "complete",
    # Error when analyzing coverage
    Error = "error",
    # No Group Policy settings in GPO
    NotApplicable = "notApplicable",

