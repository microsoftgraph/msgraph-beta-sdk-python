from enum import Enum

class Windows10AppsUpdateRecurrence(Enum):
    # Default value, specifies a single occurence.
    None_escaped = "none",
    # Daily.
    Daily = "daily",
    # Weekly.
    Weekly = "weekly",
    # Monthly.
    Monthly = "monthly",

