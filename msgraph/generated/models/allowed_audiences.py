from enum import Enum

class AllowedAudiences(Enum):
    Me = "me",
    Family = "family",
    Contacts = "contacts",
    GroupMembers = "groupMembers",
    Organization = "organization",
    FederatedOrganizations = "federatedOrganizations",
    Everyone = "everyone",
    UnknownFutureValue = "unknownFutureValue",

