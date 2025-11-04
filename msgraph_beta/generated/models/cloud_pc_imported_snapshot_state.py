from enum import Enum

class CloudPcImportedSnapshotState(str, Enum):
    NotUsed = "notUsed",
    InUse = "inUse",
    Expired = "expired",
    UnknownFutureValue = "unknownFutureValue",

