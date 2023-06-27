from enum import Enum

class DeviceScopeOperator(str, Enum):
    # No operator set for the device scope configuration.
    None_ = "none",
    # Operator for the device configuration query to be used (Equals).
    Equals = "equals",
    # Placeholder value for future expansion enums such as notEquals, contains, notContains, greaterThan, lessThan.
    UnknownFutureValue = "unknownFutureValue",

