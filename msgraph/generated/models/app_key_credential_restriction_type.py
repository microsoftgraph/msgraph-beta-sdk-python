from enum import Enum

class AppKeyCredentialRestrictionType(Enum):
    AsymmetricKeyLifetime = "asymmetricKeyLifetime",
    TrustedCertificateAuthority = "trustedCertificateAuthority",
    UnknownFutureValue = "unknownFutureValue",

