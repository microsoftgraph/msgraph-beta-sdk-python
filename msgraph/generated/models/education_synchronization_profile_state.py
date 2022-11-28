from enum import Enum

class EducationSynchronizationProfileState(Enum):
    Deleting = "deleting",
    DeletionFailed = "deletionFailed",
    ProvisioningFailed = "provisioningFailed",
    Provisioned = "provisioned",
    Provisioning = "provisioning",
    UnknownFutureValue = "unknownFutureValue",

