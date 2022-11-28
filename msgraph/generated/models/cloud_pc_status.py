from enum import Enum

class CloudPcStatus(Enum):
    NotProvisioned = "notProvisioned",
    Provisioning = "provisioning",
    Provisioned = "provisioned",
    InGracePeriod = "inGracePeriod",
    Deprovisioning = "deprovisioning",
    Failed = "failed",
    ProvisionedWithWarnings = "provisionedWithWarnings",
    Resizing = "resizing",
    Restoring = "restoring",
    PendingProvision = "pendingProvision",
    UnknownFutureValue = "unknownFutureValue",

