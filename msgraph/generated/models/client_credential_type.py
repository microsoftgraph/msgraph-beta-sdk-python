from enum import Enum

class ClientCredentialType(Enum):
    None_escaped = "none",
    ClientSecret = "clientSecret",
    ClientAssertion = "clientAssertion",
    FederatedIdentityCredential = "federatedIdentityCredential",
    ManagedIdentity = "managedIdentity",
    Certificate = "certificate",
    UnknownFutureValue = "unknownFutureValue",

