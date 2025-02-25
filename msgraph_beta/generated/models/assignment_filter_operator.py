from enum import Enum

class AssignmentFilterOperator(str, Enum):
    # Indicates operator is not set
    NotSet = "notSet",
    # Indicates the devices whose property value equals the configured input in Assignment Filters.
    Equals = "equals",
    # Indicates the devices whose property value not equals the configured input in Assignment Filters.
    NotEquals = "notEquals",
    # Indicates the devices whose property value starts with the configured input in Assignment Filters.
    StartsWith = "startsWith",
    # Indicates the devices whose property value does not start with the configured input in Assignment Filters.
    NotStartsWith = "notStartsWith",
    # Indicates the devices whose property value contains the configured input in Assignment Filters.
    Contains = "contains",
    # Indicates the devices whose property value does not contain the configured input in Assignment Filters.
    NotContains = "notContains",
    # Indicates the devices whose property value equals one of the configured input in Assignment Filters.
    In_ = "in",
    # Indicates the devices whose property value does not equals any of the configured input in Assignment Filters.
    NotIn = "notIn",
    # Indicates the devices whose property value ends with the configured input in Assignment Filters.
    EndsWith = "endsWith",
    # Indicates the devices whose property value does not end with the configured input in Assignment Filters.
    NotEndsWith = "notEndsWith",
    # Indicates the devices whose property value is greater than the configured input in Assignment Filters.
    GreaterThan = "greaterThan",
    # `Indicates the devices whose property value is greater than or equal to the configured input in Assignment Filters.
    GreaterThanOrEquals = "greaterThanOrEquals",
    # Indicates the devices whose property value is less than the configured input in Assignment Filters.
    LessThan = "lessThan",
    # Indicates the devices whose property value is less than or equal to the configured input in Assignment Filters.
    LessThanOrEquals = "lessThanOrEquals",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

