from enum import Enum

class ImportedDeviceIdentityType(Enum):
    # Unknown value of importedDeviceIdentityType.
    Unknown = "unknown",
    # Device Identity is of type imei.
    Imei = "imei",
    # Device Identity is of type serial number.
    SerialNumber = "serialNumber",

