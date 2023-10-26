from enum import Enum

class ContentState(str, Enum):
    Rest = "rest",
    Motion = "motion",
    Use = "use",

