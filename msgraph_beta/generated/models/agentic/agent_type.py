from enum import Enum

class AgentType(str, Enum):
    NotAgentic = "notAgentic",
    AgenticAppBuilder = "agenticAppBuilder",
    AgenticApp = "agenticApp",
    AgenticAppInstance = "agenticAppInstance",
    UnknownFutureValue = "unknownFutureValue",

