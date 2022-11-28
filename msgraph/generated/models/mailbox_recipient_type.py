from enum import Enum

class MailboxRecipientType(Enum):
    Unknown = "unknown",
    User = "user",
    Linked = "linked",
    Shared = "shared",
    Room = "room",
    Equipment = "equipment",
    Others = "others",

