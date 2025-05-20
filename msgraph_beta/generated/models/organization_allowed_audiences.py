from enum import Enum

class OrganizationAllowedAudiences(str, Enum):
    Me = "me",
    Organization = "organization",
    FederatedOrganizations = "federatedOrganizations",
    Everyone = "everyone",
    UnknownFutureValue = "unknownFutureValue",

