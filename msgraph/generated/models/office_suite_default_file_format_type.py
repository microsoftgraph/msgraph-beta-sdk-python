from enum import Enum

class OfficeSuiteDefaultFileFormatType(Enum):
    # No file format selected
    NotConfigured = "notConfigured",
    # Office Open XML Format selected
    OfficeOpenXMLFormat = "officeOpenXMLFormat",
    # Office Open Document Format selected
    OfficeOpenDocumentFormat = "officeOpenDocumentFormat",
    # Placeholder for evolvable enum.
    UnknownFutureValue = "unknownFutureValue",

