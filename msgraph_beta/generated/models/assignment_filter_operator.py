from enum import Enum

class AssignmentFilterOperator(str, Enum):
    # NotSet.
    NotSet = "notSet",
    # Equals.
    Equals = "equals",
    # NotEquals.
    NotEquals = "notEquals",
    # StartsWith.
    StartsWith = "startsWith",
    # NotStartsWith.
    NotStartsWith = "notStartsWith",
    # Contains.
    Contains = "contains",
    # NotContains.
    NotContains = "notContains",
    # In.
    In_ = "in",
    # NotIn.
    NotIn = "notIn",
    # EndsWith.
    EndsWith = "endsWith",
    # NotEndsWith.
    NotEndsWith = "notEndsWith",

