from enum import Enum

class AdministratorConfiguredDeviceComplianceState(Enum):
    # Set compliance state based on other compliance polices
    BasedOnDeviceCompliancePolicy = "basedOnDeviceCompliancePolicy",
    # Set compliance to nonCompliant
    NonCompliant = "nonCompliant",

