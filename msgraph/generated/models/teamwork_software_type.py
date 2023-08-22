from enum import Enum

class TeamworkSoftwareType(str, Enum):
    AdminAgent = "adminAgent",
    OperatingSystem = "operatingSystem",
    TeamsClient = "teamsClient",
    Firmware = "firmware",
    PartnerAgent = "partnerAgent",
    CompanyPortal = "companyPortal",
    UnknownFutureValue = "unknownFutureValue",

