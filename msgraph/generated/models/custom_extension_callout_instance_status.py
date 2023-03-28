from enum import Enum

class CustomExtensionCalloutInstanceStatus(Enum):
    CalloutSent = "calloutSent",
    CallbackReceived = "callbackReceived",
    CalloutFailed = "calloutFailed",
    CallbackTimedOut = "callbackTimedOut",
    WaitingForCallback = "waitingForCallback",
    UnknownFutureValue = "unknownFutureValue",

