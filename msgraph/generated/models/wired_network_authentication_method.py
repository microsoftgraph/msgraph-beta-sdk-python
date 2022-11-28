from enum import Enum

class WiredNetworkAuthenticationMethod(Enum):
    # Use an identity certificate for authentication.
    Certificate = "certificate",
    # Use username and password for authentication.
    UsernameAndPassword = "usernameAndPassword",
    # Use Derived Credential for authentication.
    DerivedCredential = "derivedCredential",
    # Sentinel member for cases where the client cannot handle the new enum values.
    UnknownFutureValue = "unknownFutureValue",

