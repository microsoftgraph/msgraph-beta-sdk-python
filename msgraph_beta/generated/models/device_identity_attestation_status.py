from enum import Enum

class DeviceIdentityAttestationStatus(str, Enum):
    # Default. Set to unknown if attestation has not yet been calculated
    Unknown = "unknown",
    # Indicates that the Device attestation is supported on the device, it was attempted on the device and the attestation has passed. The device is trusted.
    Trusted = "trusted",
    # Indicates that the Device attestation is supported on the device, it was attempted on the device and the attestation has failed. The device is untrusted
    UnTrusted = "unTrusted",
    # Indicates that the device does not support Attestation. This could be because of missing hardware or software support.
    NotSupported = "notSupported",
    # Indicates that the device did not provide with the data that were required to perform attestation.
    IncompleteData = "incompleteData",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

