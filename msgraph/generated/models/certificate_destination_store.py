from enum import Enum

class CertificateDestinationStore(Enum):
    # Computer Certificate Store - Root.
    ComputerCertStoreRoot = "computerCertStoreRoot",
    # Computer Certificate Store - Intermediate.
    ComputerCertStoreIntermediate = "computerCertStoreIntermediate",
    # User Certificate Store - Intermediate.
    UserCertStoreIntermediate = "userCertStoreIntermediate",

