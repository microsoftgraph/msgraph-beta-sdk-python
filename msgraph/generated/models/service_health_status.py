from enum import Enum

class ServiceHealthStatus(str, Enum):
    ServiceOperational = "serviceOperational",
    Investigating = "investigating",
    RestoringService = "restoringService",
    VerifyingService = "verifyingService",
    ServiceRestored = "serviceRestored",
    PostIncidentReviewPublished = "postIncidentReviewPublished",
    ServiceDegradation = "serviceDegradation",
    ServiceInterruption = "serviceInterruption",
    ExtendedRecovery = "extendedRecovery",
    FalsePositive = "falsePositive",
    InvestigationSuspended = "investigationSuspended",
    Resolved = "resolved",
    MitigatedExternal = "mitigatedExternal",
    Mitigated = "mitigated",
    ResolvedExternal = "resolvedExternal",
    Confirmed = "confirmed",
    Reported = "reported",
    UnknownFutureValue = "unknownFutureValue",

