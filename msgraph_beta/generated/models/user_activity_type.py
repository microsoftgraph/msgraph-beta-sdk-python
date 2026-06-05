from enum import Enum

class UserActivityType(str, Enum):
    UploadText = "uploadText",
    UploadFile = "uploadFile",
    DownloadText = "downloadText",
    DownloadFile = "downloadFile",
    CopyToClipboard = "copyToClipboard",
    UnknownFutureValue = "unknownFutureValue",

