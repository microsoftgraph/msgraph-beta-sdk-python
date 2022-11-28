from enum import Enum

class PlayPromptCompletionReason(Enum):
    Unknown = "unknown",
    CompletedSuccessfully = "completedSuccessfully",
    MediaOperationCanceled = "mediaOperationCanceled",
    UnknownFutureValue = "unknownFutureValue",

