from enum import Enum

class UserActivityTypes(str, Enum):
    None_ = "none",
    UploadText = "uploadText",
    UploadFile = "uploadFile",
    DownloadText = "downloadText",
    DownloadFile = "downloadFile",
    CopyToClipboard = "copyToClipboard",
    PasteFromClipboard = "pasteFromClipboard",
    Print = "print",
    AccessDebugTools = "accessDebugTools",
    UnknownFutureValue = "unknownFutureValue",

