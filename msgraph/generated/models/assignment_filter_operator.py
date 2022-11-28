from enum import Enum

class AssignmentFilterOperator(Enum):
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
    In_escaped = "in",
    # NotIn.
    NotIn = "notIn",
    # EndsWith.
    EndsWith = "endsWith",
    # NotEndsWith.
    NotEndsWith = "notEndsWith",

