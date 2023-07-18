from enum import Enum

class MonitoringAction(str, Enum):
    AlertError = "alertError",
    PauseDeployment = "pauseDeployment",
    UnknownFutureValue = "unknownFutureValue",

