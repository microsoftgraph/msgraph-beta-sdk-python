from enum import Enum

class DomainNameSource(Enum):
    # Full domain name.
    FullDomainName = "fullDomainName",
    # net bios domain name.
    NetBiosDomainName = "netBiosDomainName",

