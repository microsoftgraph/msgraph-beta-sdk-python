from enum import Enum

class VirtualEventRegistrationQuestionAnswerInputType(Enum):
    Text = "text",
    MultilineText = "multilineText",
    SingleChoice = "singleChoice",
    MultiChoice = "multiChoice",
    Boolean = "boolean",
    UnknownFutureValue = "unknownFutureValue",

