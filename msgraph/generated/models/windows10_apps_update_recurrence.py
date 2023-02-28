from enum import Enum

class Windows10AppsUpdateRecurrence(Enum):
    # Default value, specifies a single occurence.
    None_ = "none",
    # Daily.
    Daily = "daily",
    # Weekly.
    Weekly = "weekly",
    # Monthly.
    Monthly = "monthly",

