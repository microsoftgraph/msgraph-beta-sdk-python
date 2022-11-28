from enum import Enum

class AndroidManagedStoreAccountBindStatus(Enum):
    NotBound = "notBound",
    Bound = "bound",
    BoundAndValidated = "boundAndValidated",
    Unbinding = "unbinding",

