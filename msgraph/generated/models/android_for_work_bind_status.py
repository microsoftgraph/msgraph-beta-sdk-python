from enum import Enum

class AndroidForWorkBindStatus(Enum):
    NotBound = "notBound",
    Bound = "bound",
    BoundAndValidated = "boundAndValidated",
    Unbinding = "unbinding",

