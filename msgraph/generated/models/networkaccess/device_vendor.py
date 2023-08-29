from enum import Enum

class DeviceVendor(str, Enum):
    BarracudaNetworks = "barracudaNetworks",
    CheckPoint = "checkPoint",
    CiscoMeraki = "ciscoMeraki",
    Citrix = "citrix",
    Fortinet = "fortinet",
    HpeAruba = "hpeAruba",
    NetFoundry = "netFoundry",
    Nuage = "nuage",
    OpenSystems = "openSystems",
    PaloAltoNetworks = "paloAltoNetworks",
    RiverbedTechnology = "riverbedTechnology",
    SilverPeak = "silverPeak",
    VmWareSdWan = "vmWareSdWan",
    Versa = "versa",
    Other = "other",
    UnknownFutureValue = "unknownFutureValue",

