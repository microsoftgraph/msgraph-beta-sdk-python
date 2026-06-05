from enum import Enum

class UserActivityTypes(str, Enum):
    None_ = "none",
    UploadText = "uploadText",
    UploadFile = "uploadFile",
    DownloadText = "downloadText",
    DownloadFile = "downloadFile",
    CopyToClipboard = "copyToClipboard",
    UnknownFutureValue = "unknownFutureValue",

