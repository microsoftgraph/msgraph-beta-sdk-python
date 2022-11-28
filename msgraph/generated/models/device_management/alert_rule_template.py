from enum import Enum

class AlertRuleTemplate(Enum):
    CloudPcProvisionScenario = "cloudPcProvisionScenario",
    CloudPcImageUploadScenario = "cloudPcImageUploadScenario",
    CloudPcOnPremiseNetworkConnectionCheckScenario = "cloudPcOnPremiseNetworkConnectionCheckScenario",
    UnknownFutureValue = "unknownFutureValue",

