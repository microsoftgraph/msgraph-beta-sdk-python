from enum import Enum

class TenantAllowBlockListEntryType(Enum):
    Url = "url",
    FileHash = "fileHash",
    Sender = "sender",
    Recipient = "recipient",
    UnknownFutureValue = "unknownFutureValue",

