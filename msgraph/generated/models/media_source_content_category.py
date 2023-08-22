from enum import Enum

class MediaSourceContentCategory(str, Enum):
    Meeting = "meeting",
    LiveStream = "liveStream",
    Presentation = "presentation",
    ScreenRecording = "screenRecording",
    UnknownFutureValue = "unknownFutureValue",

