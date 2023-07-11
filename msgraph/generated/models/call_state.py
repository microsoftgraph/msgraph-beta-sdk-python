from enum import Enum

class CallState(str, Enum):
    Incoming = "incoming",
    Establishing = "establishing",
    Ringing = "ringing",
    Established = "established",
    Hold = "hold",
    Transferring = "transferring",
    TransferAccepted = "transferAccepted",
    Redirecting = "redirecting",
    Terminating = "terminating",
    Terminated = "terminated",
    UnknownFutureValue = "unknownFutureValue",

