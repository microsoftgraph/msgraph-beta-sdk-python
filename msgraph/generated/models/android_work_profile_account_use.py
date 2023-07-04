from enum import Enum

class AndroidWorkProfileAccountUse(str, Enum):
    # Allow additon of all accounts except Google accounts in Android Work Profile.
    AllowAllExceptGoogleAccounts = "allowAllExceptGoogleAccounts",
    # Block any account from being added in Android Work Profile. 
    BlockAll = "blockAll",
    # Allow addition of all accounts (including Google accounts) in Android Work Profile.
    AllowAll = "allowAll",
    # Unknown future value for evolvable enum patterns.
    UnknownFutureValue = "unknownFutureValue",

