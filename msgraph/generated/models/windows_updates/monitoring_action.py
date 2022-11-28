from enum import Enum

class MonitoringAction(Enum):
    AlertError = "alertError",
    PauseDeployment = "pauseDeployment",
    UnknownFutureValue = "unknownFutureValue",

