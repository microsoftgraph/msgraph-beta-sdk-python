from enum import Enum

class TenantAllowBlockListAction(Enum):
    Allow = "allow",
    Block = "block",
    UnknownFutureValue = "unknownFutureValue",

