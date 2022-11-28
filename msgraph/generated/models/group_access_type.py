from enum import Enum

class GroupAccessType(Enum):
    None_escaped = "none",
    Private = "private",
    Secret = "secret",
    Public = "public",

