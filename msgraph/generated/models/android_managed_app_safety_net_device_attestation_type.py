from enum import Enum

class AndroidManagedAppSafetyNetDeviceAttestationType(Enum):
    # no requirement set
    None_escaped = "none",
    # require that Android device passes SafetyNet Basic Integrity validation
    BasicIntegrity = "basicIntegrity",
    # require that Android device passes SafetyNet Basic Integrity and Device Certification validations
    BasicIntegrityAndDeviceCertification = "basicIntegrityAndDeviceCertification",

