from enum import Enum

class ConditionalAccessAudienceReason(str, Enum):
    None_ = "none",
    ResourcelessRequest = "resourcelessRequest",
    ConfidentialClientIdToken = "confidentialClientIdToken",
    ConfidentialClientNonIdToken = "confidentialClientNonIdToken",
    ResourceMapping = "resourceMapping",
    ResourceMappingDefault = "resourceMappingDefault",
    ScopeMapping = "scopeMapping",
    ScopeMappingDefault = "scopeMappingDefault",
    DelegatedScope = "delegatedScope",
    FirstPartyResourceDefault = "firstPartyResourceDefault",
    ThirdPartyResourceDefault = "thirdPartyResourceDefault",
    UnknownFutureValue = "unknownFutureValue",

