from enum import Enum

class CloudPcSnapshotImportFileType(str, Enum):
    DataFile = "dataFile",
    VirtualMachineGuestState = "virtualMachineGuestState",
    UnknownFutureValue = "unknownFutureValue",

