from enum import Enum

class DeploymentStateReasonValue(Enum):
    ScheduledByOfferWindow = "scheduledByOfferWindow",
    OfferingByRequest = "offeringByRequest",
    PausedByRequest = "pausedByRequest",
    PausedByMonitoring = "pausedByMonitoring",
    UnknownFutureValue = "unknownFutureValue",
    FaultedByContentOutdated = "faultedByContentOutdated",

