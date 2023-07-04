from enum import Enum

class OwnerType(str, Enum):
    # Unknown.
    Unknown = "unknown",
    # Owned by company.
    Company = "company",
    # Owned by person.
    Personal = "personal",

