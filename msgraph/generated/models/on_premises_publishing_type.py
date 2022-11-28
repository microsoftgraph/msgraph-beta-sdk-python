from enum import Enum

class OnPremisesPublishingType(Enum):
    ApplicationProxy = "applicationProxy",
    ExchangeOnline = "exchangeOnline",
    Authentication = "authentication",
    Provisioning = "provisioning",
    IntunePfx = "intunePfx",
    OflineDomainJoin = "oflineDomainJoin",
    UnknownFutureValue = "unknownFutureValue",

