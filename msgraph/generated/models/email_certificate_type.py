from enum import Enum

class EmailCertificateType(Enum):
    # Do not use a certificate as a source.
    None_escaped = "none",
    # Use an certificate for certificate source.
    Certificate = "certificate",
    # Use a derived credential for certificate source.
    DerivedCredential = "derivedCredential",

