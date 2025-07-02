from enum import Enum

class CallEventType(str, Enum):
    CallStarted = "callStarted",
    CallEnded = "callEnded",
    UnknownFutureValue = "unknownFutureValue",
    RosterUpdated = "rosterUpdated",
    TranscriptionStarted = "transcriptionStarted",
    TranscriptionStopped = "transcriptionStopped",
    RecordingStarted = "recordingStarted",
    RecordingStopped = "recordingStopped",

