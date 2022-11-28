from enum import Enum

class NonEapAuthenticationMethodForPeap(Enum):
    # None.
    None_escaped = "none",
    # Microsoft CHAP Version 2 (MS-CHAP v2).
    MicrosoftChapVersionTwo = "microsoftChapVersionTwo",

