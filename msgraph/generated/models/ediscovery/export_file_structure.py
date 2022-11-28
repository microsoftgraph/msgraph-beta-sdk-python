from enum import Enum

class ExportFileStructure(Enum):
    None_escaped = "none",
    Directory = "directory",
    Pst = "pst",
    UnknownFutureValue = "unknownFutureValue",

