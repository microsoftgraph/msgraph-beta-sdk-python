from enum import Enum

class CertificateRevocationStatus(Enum):
    # Not revoked.
    None_escaped = "none",
    # Revocation pending.
    Pending = "pending",
    # Revocation command issued.
    Issued = "issued",
    # Revocation failed.
    Failed = "failed",
    # Revoked.
    Revoked = "revoked",

