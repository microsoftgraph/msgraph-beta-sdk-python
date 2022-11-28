from enum import Enum

class RecordCompletionReason(Enum):
    OperationCanceled = "operationCanceled",
    StopToneDetected = "stopToneDetected",
    MaxRecordDurationReached = "maxRecordDurationReached",
    InitialSilenceTimeout = "initialSilenceTimeout",
    MaxSilenceTimeout = "maxSilenceTimeout",
    PlayPromptFailed = "playPromptFailed",
    PlayBeepFailed = "playBeepFailed",
    MediaReceiveTimeout = "mediaReceiveTimeout",
    UnspecifiedError = "unspecifiedError",

