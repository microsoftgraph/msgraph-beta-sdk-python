from enum import Enum

class AlertRuleTemplate(str, Enum):
    CloudPcProvisionScenario = "cloudPcProvisionScenario",
    CloudPcImageUploadScenario = "cloudPcImageUploadScenario",
    CloudPcOnPremiseNetworkConnectionCheckScenario = "cloudPcOnPremiseNetworkConnectionCheckScenario",
    UnknownFutureValue = "unknownFutureValue",
    CloudPcInGracePeriodScenario = "cloudPcInGracePeriodScenario",
    CloudPcFrontlineInsufficientLicensesScenario = "cloudPcFrontlineInsufficientLicensesScenario",

