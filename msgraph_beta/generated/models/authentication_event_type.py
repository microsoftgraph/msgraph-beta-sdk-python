from enum import Enum

class AuthenticationEventType(str, Enum):
    TokenIssuanceStart = "tokenIssuanceStart",
    PageRenderStart = "pageRenderStart",
    UnknownFutureValue = "unknownFutureValue",

