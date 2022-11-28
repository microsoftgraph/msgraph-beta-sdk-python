from enum import Enum

class SharingDomainRestrictionMode(Enum):
    None_escaped = "none",
    AllowList = "allowList",
    BlockList = "blockList",
    UnknownFutureValue = "unknownFutureValue",

