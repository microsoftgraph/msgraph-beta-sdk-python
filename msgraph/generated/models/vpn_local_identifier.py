from enum import Enum

class VpnLocalIdentifier(Enum):
    # Device Fully Qualified Domain Name
    DeviceFQDN = "deviceFQDN",
    # Empty
    Empty = "empty",
    # Client Certificate Subject Name
    ClientCertificateSubjectName = "clientCertificateSubjectName",

