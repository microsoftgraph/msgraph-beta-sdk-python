from enum import Enum

class ITunesPairingMode(Enum):
    # Pairing is not allowed
    Disallow = "disallow",
    # Pairing allowed
    Allow = "allow",
    # Certificate required to pair with iTunes
    RequiresCertificate = "requiresCertificate",

