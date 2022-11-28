from enum import Enum

class ExportOptions(Enum):
    OriginalFiles = "originalFiles",
    Text = "text",
    PdfReplacement = "pdfReplacement",
    FileInfo = "fileInfo",
    Tags = "tags",
    UnknownFutureValue = "unknownFutureValue",

