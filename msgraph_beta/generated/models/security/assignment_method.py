from enum import Enum

class AssignmentMethod(str, Enum):
    Standard = "standard",
    Privileged = "privileged",
    Auto = "auto",

