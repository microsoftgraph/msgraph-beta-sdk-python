from enum import Enum

class DeviceComplianceScriptRuleDataType(Enum):
    # None data type.
    None_escaped = "none",
    # Boolean data type.
    Boolean = "boolean",
    # Int64 data type.
    Int64 = "int64",
    # Double data type.
    Double = "double",
    # String data type.
    String = "string",
    # DateTime data type.
    DateTime = "dateTime",
    # Version data type.
    Version = "version",
    # Base64 data type.
    Base64 = "base64",
    # Xml data type.
    Xml = "xml",
    # Boolean array data type.
    BooleanArray = "booleanArray",
    # Int64 array data type.
    Int64Array = "int64Array",
    # Double array data type.
    DoubleArray = "doubleArray",
    # String array data type.
    StringArray = "stringArray",
    # DateTime array data type.
    DateTimeArray = "dateTimeArray",
    # Version array data type.
    VersionArray = "versionArray",

