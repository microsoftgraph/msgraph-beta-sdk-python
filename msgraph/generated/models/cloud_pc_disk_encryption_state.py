from enum import Enum

class CloudPcDiskEncryptionState(Enum):
    NotAvailable = "notAvailable",
    NotEncrypted = "notEncrypted",
    EncryptedUsingPlatformManagedKey = "encryptedUsingPlatformManagedKey",
    EncryptedUsingCustomerManagedKey = "encryptedUsingCustomerManagedKey",
    UnknownFutureValue = "unknownFutureValue",

