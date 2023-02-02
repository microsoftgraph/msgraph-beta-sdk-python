from enum import Enum

class ClientCredentialType(Enum):
    None_ = "none",
    ClientSecret = "clientSecret",
    ClientAssertion = "clientAssertion",
    FederatedIdentityCredential = "federatedIdentityCredential",
    ManagedIdentity = "managedIdentity",
    Certificate = "certificate",
    UnknownFutureValue = "unknownFutureValue",

