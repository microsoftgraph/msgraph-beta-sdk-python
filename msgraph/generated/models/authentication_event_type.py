from enum import Enum

class AuthenticationEventType(Enum):
    TokenIssuanceStart = "tokenIssuanceStart",
    PageRenderStart = "pageRenderStart",
    UnknownFutureValue = "unknownFutureValue",

