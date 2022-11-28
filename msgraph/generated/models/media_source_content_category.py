from enum import Enum

class MediaSourceContentCategory(Enum):
    Meeting = "meeting",
    LiveStream = "liveStream",
    Presentation = "presentation",
    ScreenRecording = "screenRecording",
    UnknownFutureValue = "unknownFutureValue",

