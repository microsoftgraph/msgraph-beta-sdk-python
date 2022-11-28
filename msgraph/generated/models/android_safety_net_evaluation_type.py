from enum import Enum

class AndroidSafetyNetEvaluationType(Enum):
    # Default value. Typical measurements and reference data were used.
    Basic = "basic",
    # Hardware-backed security features (such as Key Attestation) were used.
    HardwareBacked = "hardwareBacked",

